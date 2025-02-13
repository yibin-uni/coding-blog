import requests
import feedparser
import json
from pathlib import Path

def fetch_arxiv_papers(keywords, max_results=10):
    query = " OR ".join([f'(ti:"{kw}" OR abs:"{kw}")' for kw in keywords])
    url = f"http://export.arxiv.org/api/query?search_query={query}&sortBy=submittedDate&sortOrder=descending&max_results={max_results}"

    response = requests.get(url)
    feed = feedparser.parse(response.text)

    papers = []
    for entry in feed.entries:
        papers.append({
            "title": entry.title,
            "authors": ", ".join(author.name for author in entry.authors),
            "summary": entry.summary,
            "published": entry.published,
            "pdf_link": entry.link.replace("abs", "pdf")
        })
    return papers

if __name__ == "__main__":
    keywords = ["causal inference", "causal", "graph neural network"]
    papers = fetch_arxiv_papers(keywords, max_results=10)
    
    data_path = Path("data")
    data_path.mkdir(exist_ok=True)
    
    with open(data_path / "papers.json", "w") as f:
        json.dump(papers, f, indent=2)

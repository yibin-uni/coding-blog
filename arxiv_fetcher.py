import requests
import feedparser

def fetch_arxiv_papers(keywords, max_results=10):
    # Let's add quotation marks for exact match of phrases
    query = " OR ".join([f'(ti:"{kw}" OR abs:"{kw}")' for kw in keywords])
    print(query)
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

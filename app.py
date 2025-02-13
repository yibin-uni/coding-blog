from flask import Flask, render_template
from arxiv_fetcher import fetch_arxiv_papers  # Import the function

app = Flask(__name__)

@app.route("/")
def main_page():
    return render_template("index.html")

@app.route("/pacman")
def pacman_game():
    return render_template("pacman_game.html")

@app.route("/arxiv")
def show_papers():
    keywords = ["causal inference", "causal", "graph neural network"]
    papers = fetch_arxiv_papers(keywords, max_results=10)
    return render_template("papers.html", papers=papers)

if __name__ == "__main__":
    app.run(debug=True)

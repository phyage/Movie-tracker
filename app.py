
from flask import Flask, render_template, request
import requests
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def home():

    results = []

    if request.method == "POST":

        movie_search = request.form.get("movie_search")

        api_key = os.environ.get("TMDB_API_KEY")

        url = "https://api.themoviedb.org/3/search/movie"

        parameters = {
            "api_key": api_key,
            "query": movie_search
        }

        response = requests.get(url, params=parameters)

        data = response.json()

        results = data.get("results", [])

    return render_template("index.html", results=results)


if __name__ == "__main__":
    app.run(debug=True)

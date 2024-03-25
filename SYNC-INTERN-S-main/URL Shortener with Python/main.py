import json
import random
import string
from flask import Flask, request, render_template, redirect

app = Flask(__name__)

SHORTENED_URL_FILE = "shortened_urls.json"

shortened_url = {}

def generate_short_url(length=6):
    chars = string.ascii_letters + string.digits
    short_url = ''.join(random.choice(chars) for _ in range(length))
    return short_url

def save_shortened_urls():
    with open(SHORTENED_URL_FILE, "w") as f:
        json.dump(shortened_url, f)

def load_shortened_urls():
    try:
        with open(SHORTENED_URL_FILE, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return {}

@app.route('/', methods=['GET', 'POST'])
def index():
    short_url = None  # Initialize short_url variable
    if request.method == "POST":
        long_url = request.form['long_url']
        short_url = generate_short_url()
        while short_url in shortened_url:
            short_url = generate_short_url()
        shortened_url[short_url] = long_url
        save_shortened_urls()
    return render_template('index.html', short_url=short_url)


@app.route('/<short_url>')
def redirect_to_url(short_url):
    shortened_url = load_shortened_urls()
    long_url = shortened_url.get(short_url)
    if long_url:
        return redirect(long_url)
    else:
        return "Invalid URL", 404

if __name__ == "__main__":
    shortened_url = load_shortened_urls()
    app.run(debug=True)

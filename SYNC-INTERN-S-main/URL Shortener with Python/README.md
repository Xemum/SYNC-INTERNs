# URL Shortener

This is a simple URL shortener web application built with Flask. It allows users to shorten long URLs into shorter ones.

## Features

- Shorten long URLs into shorter ones.
- Redirect users to the original URL when they visit the shortened URL.

## Requirements

- Python 3.x
- Flask

## Installation

1. Clone the repository
2. Install Flask : pip install flask
3. Run the application:


## Usage

- Navigate to `http://localhost:5000` in your web browser.
- Enter the long URL you want to shorten in the input field.
- Click the "Shorten URL" button.
- The shortened URL will be displayed below.
- You can click on the shortened URL to be redirected to the original URL.

## Files

- `app.py`: Contains the Flask application code.
- `index.html`: HTML template for the index page.

## Code Overview

- `generate_short_url()`: Generates a random short URL.
- `save_shortened_urls()`: Saves the shortened URLs to a JSON file.
- `load_shortened_urls()`: Loads the shortened URLs from the JSON file.
- `/`: Route for the index page where users can shorten URLs.
- `/<short_url>`: Route for redirecting users to the original URL based on the shortened URL.

## Notes

- Shortened URLs are stored in a JSON file (`shortened_urls.json`).
- The length of the shortened URL can be adjusted by modifying the `length` parameter in `generate_short_url()` function.

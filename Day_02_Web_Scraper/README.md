# Day 02 - Web Scraper

## Project Description

This project implements a basic web scraper using Python's `requests` and `BeautifulSoup4` libraries. It allows users to input a URL and then extracts all `<title>` tags from the specified webpage. This serves as a foundational example for more complex web scraping tasks.

## Features

*   **URL Input**: Prompts the user to enter a URL to scrape.
*   **HTTP Request Handling**: Uses `requests` to fetch the content of the webpage.
*   **HTML Parsing**: Employs `BeautifulSoup4` to parse the HTML content.
*   **Title Extraction**: Specifically targets and extracts the text content of all `<title>` tags.
*   **Error Handling**: Includes basic error handling for network requests.

## How to Run

1.  **Navigate to the project directory**:

    ```bash
    cd "30-days-of-projects/Day_02_Web_Scraper"
    ```

2.  **Install dependencies**:

    ```bash
    pip install requests beautifulsoup4
    ```

3.  **Run the web scraper**:

    ```bash
    python web_scraper.py
    ```

## Usage

Upon running the script, you will be prompted to enter a URL:

```
Enter the URL to scrape (e.g., https://www.google.com): https://www.example.com

Scraping https://www.example.com...

Extracted Titles:
- Example Domain
```

If no titles are found or an error occurs during the request, appropriate messages will be displayed.

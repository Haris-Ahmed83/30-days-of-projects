
import requests
from bs4 import BeautifulSoup

def scrape_website(url):
    """
    Scrapes a given URL and extracts all the title tags.
    """
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an HTTPError for bad responses (4xx or 5xx)
    except requests.exceptions.RequestException as e:
        return f"Error during request to {url}: {e}"

    soup = BeautifulSoup(response.text, 'html.parser')
    titles = soup.find_all('title') # Example: find all title tags
    
    extracted_data = []
    for title in titles:
        extracted_data.append(title.get_text())

    return extracted_data

if __name__ == "__main__":
    target_url = input("Enter the URL to scrape (e.g., https://www.google.com): ")
    if not target_url.startswith(('http://', 'https://')):
        target_url = 'https://' + target_url

    print(f"\nScraping {target_url}...")
    data = scrape_website(target_url)
    
    if isinstance(data, list):
        if data:
            print("\nExtracted Titles:")
            for item in data:
                print(f"- {item}")
        else:
            print("No titles found on the page.")
    else:
        print(data)

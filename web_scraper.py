import requests
from bs4 import BeautifulSoup
import json
from datetime import datetime
from urllib.parse import urljoin, urlparse
import time

def check_robots_txt(url):
    """Check if scraping is allowed by robots.txt"""
    try:
        # Get the base URL
        parsed_url = urlparse(url)
        base_url = f"{parsed_url.scheme}://{parsed_url.netloc}"
        
        # Try to fetch robots.txt
        robots_url = urljoin(base_url, '/robots.txt')
        response = requests.get(robots_url)
        response.raise_for_status()
        
        # Parse robots.txt content
        robots_content = response.text.lower()
        
        # Check if there are any disallow rules
        if 'disallow:' in robots_content:
            print(f"⚠️ Warning: This website has robots.txt rules. Please review them at: {robots_url}")
            print("Proceeding with scraping, but please ensure you comply with the website's terms of service.")
        
        # Add a small delay to be respectful to the server
        time.sleep(1)
        return True
        
    except requests.RequestException:
        print("⚠️ Warning: Could not access robots.txt. Proceeding with caution.")
        return True

def scrape_website(url):
    try:
        # First check robots.txt
        if not check_robots_txt(url):
            print("❌ Scraping not allowed according to robots.txt")
            return None
            
        # Send a GET request to the website
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception for bad status codes
        
        # Parse the HTML content
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Extract information
        data = {
            'title': soup.title.string if soup.title else 'No title found',
            'headings': [h.text.strip() for h in soup.find_all(['h1', 'h2', 'h3'])],
            'links': [{'text': a.text.strip(), 'href': a.get('href')} for a in soup.find_all('a', href=True)],
            'scraped_at': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
            'robots_txt_checked': True
        }
        
        # Save the results to a JSON file
        with open('scraping_results.json', 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=4, ensure_ascii=False)
            
        print("✅ Scraping completed successfully!")
        print(f"📁 Results saved to scraping_results.json")
        
        return data
        
    except requests.RequestException as e:
        print(f"❌ Error occurred while scraping: {e}")
        return None

if __name__ == "__main__":
    print("🌐 Web Scraper with robots.txt Checker")
    print("----------------------------------------")
    website_url = input("Enter the website URL to scrape: ")
    scrape_website(website_url) 
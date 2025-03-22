# Web Scraper Portfolio Project

A simple and efficient web scraper built with Python that extracts basic information from websites. This project demonstrates fundamental web scraping concepts, data extraction techniques, and ethical scraping practices.

## Features

- Extracts website title
- Collects all headings (h1, h2, h3)
- Gathers all links with their text and URLs
- Saves results in a structured JSON format
- Error handling for failed requests
- Timestamp tracking for each scraping operation
- **Ethical Scraping Features**:
  - Automatic robots.txt checking
  - Respects website crawling policies
  - Rate limiting to prevent server overload
  - Clear warnings about scraping permissions

## Prerequisites

- Python 3.6 or higher
- pip (Python package installer)

## Installation

1. Clone this repository:
```bash
git clone https://github.com/UTGyan7/web-scraper
cd web-scraper
```

2. Install the required packages:
```bash
pip install -r requirements.txt
```

## Usage

1. Run the script:
```bash
python web_scraper.py
```

2. Enter the website URL when prompted

3. The script will:
   - Check the website's robots.txt file
   - Display any warnings about scraping permissions
   - Proceed with scraping if allowed
   - Save results in `scraping_results.json`

## Output Format

The scraper generates a JSON file with the following structure:
```json
{
    "title": "Website Title",
    "headings": ["Heading 1", "Heading 2", ...],
    "links": [
        {
            "text": "Link Text",
            "href": "https://example.com"
        },
        ...
    ],
    "scraped_at": "2024-03-21 15:30:00",
    "robots_txt_checked": true
}
```

## Ethical Scraping Guidelines

This scraper follows these ethical practices:
1. Checks robots.txt before scraping
2. Respects website crawling policies
3. Implements rate limiting (1-second delay between requests)
4. Provides clear warnings about potential legal issues
5. Maintains transparency about the scraping process

## Contributing

Feel free to submit issues and enhancement requests!

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Author

Your Name
- GitHub: [Your GitHub Profile]
- LinkedIn: [Your LinkedIn Profile]

## Acknowledgments

- BeautifulSoup4 for HTML parsing
- Requests library for HTTP requests
- Robots.txt protocol for ethical web scraping guidelines 

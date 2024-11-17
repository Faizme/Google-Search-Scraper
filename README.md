# Google Search Scraper

Google Search Scraper is a Python script that allows you to extract Google search results, including titles, links, and descriptions, using the `requests` and `BeautifulSoup` libraries. This tool is useful for research, SEO analysis, and data gathering.

## Features
- Extracts top search results from Google.
- Retrieves the title, URL, and a short description for each result.
- Customizable number of results to fetch.

## Prerequisites
- Python 3.x
- The following Python libraries:
  - `requests`
  - `beautifulsoup4`

You can install the dependencies using:
```
pip install requests beautifulsoup4
```
### Usage
---
1. Clone the repository:
```
git clone https://github.com/Faizme/Google-Search-Scraper.git
```
2. Navigate to the project directory:
```
cd google-search-scraper
```
3. Run the script:
```
python webscrap.py
```
4. Input the search query and the number of results when prompted.

### Example Output
---
```
Query: Python programming
Number of Results: 5
1. Python.org: Python Programming Language
   Link: https://www.python.org
   Description: Python is a programming language that lets you work quickly...

2. Learn Python - Codecademy
   Link: https://www.codecademy.com/learn/learn-python
   Description: Learn Python, a powerful language used by sites like YouTube...
```

### Notes
---
* This script relies on Google’s current HTML structure, which may change over time.
* Frequent scraping may result in CAPTCHA challenges or temporary IP bans. Consider using proxies and request throttling if running this script at scale.

### Legal Disclaimer
---
This script is for educational purposes only. Scraping Google search results may violate their Terms of Service. Use this script responsibly.

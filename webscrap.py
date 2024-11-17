from bs4 import BeautifulSoup
import requests
import urllib.parse

# Function to scrape Google search results
def google_search(query, num_results=10):
    # Base URL for Google search
    base_url = "https://www.google.com/search"
    
    # Request headers to mimic a real browser and avoid detection
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36"
    }
    
    # Parameters for the search query and the number of results
    params = {
        "q": query,
        "num": num_results
    }
    
    # Send the GET request and capture the response
    response = requests.get(base_url, headers=headers, params=params)
    
    # Check if the request was successful
    if response.status_code != 200:
        print("Failed to retrieve results")
        return []
    
    # Parse the HTML content using BeautifulSoup
    soup = BeautifulSoup(response.text, "html.parser")
    
    # List to store the extracted search results
    results = []
    
    # Extract search result details using CSS selectors
    for result in soup.select('.tF2Cxc'):
        title = result.select_one('h3')  # Extract the title
        link = result.select_one('a')  # Extract the URL
        description = result.select_one('.VwiC3b')  # Extract the description
        
        if title and link and description:
            results.append({
                "title": title.get_text(),
                "link": link['href'],
                "description": description.get_text()
            })
    
    # Handle cases where no results are found
    if not results:
        print("No results found")

    return results

# Input query and the number of results to fetch
query = input("Query: ")
num_results = int(input("Number of Results: "))

# Fetch and display the search results
results = google_search(query, num_results)
for idx, result in enumerate(results, start=1):
    print(f"{idx}. {result['title']}")
    print(f"  Link: {result['link']}")
    print(f"  Description: {result['description']}\n")

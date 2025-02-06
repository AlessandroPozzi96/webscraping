import cloudscraper
from bs4 import BeautifulSoup

# URL of the forum page
url = "https://www.jeuxvideo.com/forums/0-51-0-1-0-1-0-blabla-18-25-ans.htm"

# Create a scraper to bypass protections
scraper = cloudscraper.create_scraper()
response = scraper.get(url)

if response.status_code == 200:
    soup = BeautifulSoup(response.content, "html.parser")

    # Extract list items with data-id attribute
    topic_elements = soup.find_all("li", {"data-id": True})

    print("List of Topics:")
    print("=" * 40)

    for idx, topic in enumerate(topic_elements, start=1):
        # Directly find <a> with 'title' attribute
        title_element = topic.find("a", {"title": True})  # Look for an <a> tag with a 'title' attribute
        if title_element:
            print(f"{idx}. {title_element['title']}")  # Print the value of the 'title' attribute
else:
    print(f"Failed to fetch page, status: {response.status_code}")

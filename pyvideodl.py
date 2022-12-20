import requests
from bs4 import BeautifulSoup

# URL of the web page to crawl
url = "https://example.com"

# Send a GET request to the URL and get the HTML response
response = requests.get(url)

# Parse the response using BeautifulSoup
soup = BeautifulSoup(response.text, "html.parser")

# Find all the links on the page
links = soup.find_all("a")

# Iterate over the links and check if they point to a video file
for link in links:
    href = link.get("href")
    if href.endswith(".flv") or href.endswith(".mp4") or href.endswith(".avi"):
# Download the video file
        video_data = requests.get(href)

# Save the video file to disk
        with open("video.flv", "wb") as f:
            f.write(video_data.content)

        print("Saved video to disk:", href)

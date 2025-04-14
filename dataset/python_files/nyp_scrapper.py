# File is intended to scrape article titles off Fox News
# Thomas Lukasiewicz
import requests
import csv
from bs4 import BeautifulSoup

# Declare URL
url = "https://nypost.com"

# Send a GET request
headers = {"User-Agent": "Mozilla/5.0"}
response = requests.get(url, headers=headers)

# Parse HTML content
soup = BeautifulSoup(response.text, "lxml")

# Extract article titles
articles = soup.find_all("h3", class_="headline")
nyp_titles = []

for index, article in enumerate(articles, start=1):
    nyp_titles.append(f"{index}. {article.text.strip()}")

# CSV setup and write to file
csv_filename = "nyp_news_titles.csv"

with open(csv_filename, "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    for title in nyp_titles:
        writer.writerow([title])

print(f"Scraped {len(nyp_titles)} article titles and saved to {csv_filename}")
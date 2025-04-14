# File is intended to scrape article titles off BBC News
# Thomas Lukasiewicz
import requests
import csv
from bs4 import BeautifulSoup

# Declare URL
url = "https://www.bbc.com"

# Send GET request
headers = {"User-Agent": "Mozilla/5.0"}
response = requests.get(url, headers=headers)

# Parse the HTML
soup = BeautifulSoup(response.text, "lxml")

# Find headline elements, these may change in some form day to day, hard to say.
articles = soup.find_all("h2", class_=("sc-87075214-3 dVjkXg", "sc-87075214-3 eywmDE"))
bbc_titles = []

for index, article in enumerate(articles, start=1):
    bbc_titles.append(f"{index}. {article.text.strip()}")

# CSV setup and write to file
csv_filename = "bbc_news_titles.csv"

with open(csv_filename, "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    for title in bbc_titles:
        writer.writerow([title])

print(f"Scraped {len(bbc_titles)} article titles and saved to {csv_filename}")
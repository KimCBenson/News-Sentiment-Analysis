# File is intended to scrape article titles off Fox News
# Thomas Lukasiewicz
import requests
from bs4 import BeautifulSoup
import csv

# Initial Setup
url = "https://www.foxnews.com/"
headers = {"User-Agent": "Mozilla/5.0"}

# Send GET request and parse
response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.text, "html.parser")

# Extract all article titles
fn_titles = []

for headline in soup.find_all(["h3"]):
    link = headline.find("a")  # Get the link inside the heading
    if link and link.text.strip():
        fn_titles.append(link.text.strip())

# csv file declaration and setup
csv_filename = "fox_news_titles.csv"

with open(csv_filename, "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    for title in fn_titles:
        writer.writerow([title])

print(f"Scraped {len(fn_titles)} article titles and saved to {csv_filename}")

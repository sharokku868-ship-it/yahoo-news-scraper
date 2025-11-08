import requests
from bs4 import BeautifulSoup
import csv

URL = "https://news.yahoo.co.jp/"

response = requests.get(URL)
soup = BeautifulSoup(response.text, "html.parser")

news_items = soup.select("a.sc-d9e4c7bc-0")  

with open("news.csv", mode="w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(["タイトル", "リンク"])
    for item in news_items[:10]:
        title = item.get_text(strip=True)
        link = item.get("href")
        writer.writerow([title, link])

print("news.csv にニュース情報を保存しました。")

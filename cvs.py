import requests
from bs4 import BeautifulSoup
import csv

url = "http://books.toscrape.com/"

def scrape_books(url):
    response = requests.get(url)
    if response.status_code != 200:
        print("Cannot fetch data")
        return []  
    response.encoding = response.apparent_encoding
    books = []

    soup = BeautifulSoup(response.text, "html.parser")
    articles = soup.find_all("article", class_="product_pod")

    for article in articles:
        title = article.h3.a['title']
        print(title)  # Optional debug

        price_text = article.find("p", class_='price_color').text
        print(price_text, type(price_text))  # Optional debug

        currency = price_text[0]
        price = float(price_text[1:])

        print(title, currency, price)  

        books.append({
            "title": title,
            "price": price,
            "currency": currency
        })

    return books


all_books = scrape_books(url)


if all_books:
    with open("books.csv", "w", newline='', encoding="utf-8", ) as f:
        writer = csv.DictWriter(f, fieldnames=["title", "price", "currency"])
        writer.writeheader()
        writer.writerows(all_books)

    print(" Books saved successfully to books.csv")
else:
    print(" No books scraped. Please check your connection or the URL.")

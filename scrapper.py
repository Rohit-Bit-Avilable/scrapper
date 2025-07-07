import json
import requests
from bs4 import BeautifulSoup

url = "http://books.toscrape.com/"

def scrape_books(url):
    response = requests.get(url)
    if response.status_code != 200:
        print("Cannot fetch data")
        return []  # Return empty list if failed

    response.encoding = response.apparent_encoding
    books = []

    soup = BeautifulSoup(response.text, "html.parser")
    articles = soup.find_all("article", class_="product_pod")
    # print(articles)  # Debug only, can remove if you want clean output

    for article in articles:
        title = article.h3.a['title']
        print(title)  # Optional debug

        price_text = article.find("p", class_='price_color').text
        print(price_text, type(price_text))  # Optional debug

        currency = price_text[0]
        price = float(price_text[1:])

        print(title, currency, price)  # Optional debug

        books.append({
            "title": title,
            "price": price,
            "currency": currency
        })

    return books 
 #  moved outside the loop

# Call scraping function
all_books = scrape_books(url)

# Save to JSON if data is fetched
if all_books:
    with open("books.json", "w", encoding="utf-8") as f:
        json.dump(all_books, f, indent=2, ensure_ascii=False)

    print(" Books saved successfully to books.json")
else:
    print(" No books scraped. Please check your connection or the URL.")
#git config --global user.name "Rohit Adhikari"
# git config --global user.email "adhikarirohit247@gmail.com"
#git init
#git status=>to check the file in status
#git diff=>to check the change in code
#git add .
#git commit "your mrssage"
#gfsudhfui
#hfuisdhgu
#dhfisd



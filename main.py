import requests
from bs4 import BeautifulSoup

URL = "https://books.toscrape.com/"
BOOK_PAGE = "ol.row li.col-xs-6.col-sm-4.col-md-3.col-lg-3"
TITLE = "article.product_pod h3 a"
PRICE = "div.product_price p.price_color"
RATING = "p:nth-of-type(1)"
IMAGES = "div.image_container a img"
page = requests.get(URL)

soup = BeautifulSoup(page.content, "html.parser")

for counter, book in enumerate(soup.select(BOOK_PAGE), start=1):
    book_title = book.select_one(TITLE).attrs["title"]
    book_price = book.select_one(PRICE).string
    book_star = book.select_one(RATING).attrs["class"]
    book_rating = [x for x in book_star if x != 'star-rating'][0]
    book_image = book.select_one(IMAGES).attrs['src']
    img_links = URL + book_image
    content = requests.get(img_links).content
    with open(f"images/book{counter}.png", "wb") as f:
        f.write(content)
    print(book_image)

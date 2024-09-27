import requests
from bs4 import BeautifulSoup
import pandas as pd
books = []
for i in range(1,5):

    url = f"https://books.toscrape.com/catalogue/page-{i}.html"

    response = requests.get(url)

    soup = BeautifulSoup(response.content,'html.parser')

    ol = soup.find('ol',class_='row')

    articles = ol.find_all('article',class_='product_pod')
    for article in articles:
        image = article.find('img')
        title = image.attrs['alt']
        star = article.find('p')
        star = star['class'][1]
        price = float(article.find('p',class_='price_color').text[1:])
        books.append([title,price,star])

df = pd.DataFrame(books,columns=['Title','Price','Rating'])
df.to_csv('books.csv')
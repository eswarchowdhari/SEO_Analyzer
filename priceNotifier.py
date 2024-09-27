import requests
from bs4 import BeautifulSoup
import smtplib 
re = requests.get("https://www.amazon.in/s?k=headphones&rh=n%3A1389401031&ref=nb_sb_noss")
res = re.content
soup = BeautifulSoup(res,'html.parser')
prices = soup.find_all('span',class_='a-price-whole')
for pric in prices:
    print({pric.text})
if price < 60:
    smt = smtplib.SMTP('smtp.gmail.com',587)
     smt.ehlo()
     smt.starttls() # used for security purpose
     smt.login('saieswarchowdhari@gmail.com','kxhy kwft qaoo ymsc')
     smt.sendmail('saieswarchowdhari@gmail.com','chidarasaipranay789@gmail.com',
                  f"Subject: Book Price Notifier\n\nHi, price has dropped to {price}. Buy it Now!")
     smt.quit()
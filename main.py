import requests
import lxml
from bs4 import BeautifulSoup
import smtplib

amazon_url = "https://www.amazon.com/Instant-Pot-Ultra-Programmable-Sterilizer/dp/B06Y1MP2PY/ref=sr_1_8?crid=1UUNHTFB61PE5&keywords=instant+pot&qid=1679750379&sprefix=instant+p%2Caps%2C238&sr=8-8"

headers ={
    "User-Agent":"Defined",
    "Accept-Language" : "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
}

my_email = "REPLACE"
password = "REPLACE"

response = requests.get(url=amazon_url, headers=headers)

soup = BeautifulSoup(response.text, "lxml")

price_class = soup.find("span", {"class": "a-offscreen"})
price = price_class.text.strip()
floating_price = float(price.replace("$", ""))
print(floating_price)
target_price = float(100)

title_class = soup.find("span", {"class": "a-size-large product-title-word-break"})
title = title_class.text.strip()

if floating_price <= target_price:
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email, to_addrs="REPLACE", msg=f"subject:Low Price Alert\n\n{title} now only ${floating_price}.\nLink: {amazon_url}".encode('utf-8'))
        print("Done")
    
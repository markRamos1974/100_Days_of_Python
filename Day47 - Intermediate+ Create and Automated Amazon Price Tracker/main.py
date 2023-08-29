from bs4 import BeautifulSoup
import requests
from dotenv import load_dotenv
import os
import smtplib

load_dotenv()
URL = os.environ.get("ITEM_URL")
target_price = 100


requests_headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36",
    "Accept-Language": "en-GB,en-US;q=0.0.en;q=0.8" 
}
response = requests.get(url="https://www.amazon.com/dp/B075CYMYK6?psc=1&ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6", headers=requests_headers)
response = response.text

soup = BeautifulSoup(response, "html.parser")
whole_price = soup.find(name="span", class_="a-price-whole").getText()
decimal_price = soup.find(name="span", class_="a-price-fraction").getText()
product_name = soup.find(name="span", id="productTitle", class_="product-title-word-break").getText().strip()

price = float(f"{whole_price}{decimal_price}")



APP_PASSWORD = os.environ.get("APP_PASSWORD")
EMAIL= os.environ.get("MY_EMAIL")
RECIEPIENT = os.environ.get("RECIEPIENT")

if price < target_price:

    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        message = f"{product_name} is now ${price}, BUY NOW!".encode("utf-8")
        connection.starttls()
        connection.login(user=EMAIL, password=APP_PASSWORD)
        connection.sendmail(from_addr=EMAIL, to_addrs=RECIEPIENT, msg=message)
from bs4 import BeautifulSoup
import requests
from dotenv import load_dotenv
import os
import smtplib

# create your own env
load_dotenv("mail.env")
my_email = os.getenv("MY_EMAIL")
smtp = os.getenv("SMTP")
password = os.getenv("PASSWORD")
port = int(os.getenv("PORT"))
link = "https://www.tokopedia.com/doremimusik/keyboard-casio-ctx-700-original-tanpa-paket?extParam=ivf%3Dfalse%26src%3Dsearch&refined=true"

response = requests.get("https://www.tokopedia.com/doremimusik/keyboard-casio-ctx-700-original-tanpa-paket?extParam=ivf%3Dfalse%26src%3Dsearch&refined=true", headers={"Accept-Language":"en-US,en;q=0.9", "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36"})
response.raise_for_status
ctx_700_page = response.text
warning_price = 2700000

# print(ctx_700_page)
soup = BeautifulSoup(ctx_700_page, "html.parser")
price_obj = soup.find(name="div", class_="price")
# print(price)

price_text = price_obj.getText().strip("Rp.").replace(".","")
price = int(price_text)

def send_warning(low_price):
    connection=smtplib.SMTP(smtp, port)
    connection.starttls()
    connection.login(user=my_email, password=password)
    connection.sendmail(
        from_addr=my_email,
        to_addrs=my_email,
        msg=f"Subject: Casio CTX 700 Lowest Price\n\nNew Lowest Price for Casio CTX700\nLink : {link}\nPrice : Rp.{low_price}"
    )   
        
    

if price <= warning_price:
    send_warning(price)
    warning_price = price  # probably should keep this on a .txt file

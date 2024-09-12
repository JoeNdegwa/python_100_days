from bs4 import BeautifulSoup
import requests
import smtplib
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()
"""
SMTP_ADDRESS="smtp.gmail.com"
EMAIL_ADDRESS="your_email@email.com"
EMAIL_PASSWORD="your app password"
"""

# Live Site
url = "https://www.amazon.com/dp/B075CYMYK6?psc=1&ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6"

# ====================== Add Headers to the Request ===========================

header = {
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.9"
}

# Adding headers to the request
response = requests.get(url, headers=header)

soup = BeautifulSoup(response.content, "html.parser")
# Check you are getting the actual Amazon page back and not something else:
print(soup.prettify())

# Find the HTML element that contains the price
price = soup.find(class_="a-offscreen").get_text()

# Remove the dollar sign using split
price_without_currency = price.split("$")[1]

# Convert to floating point number
price_as_float = float(price_without_currency)
print(price_as_float)

# Get the product title
title = soup.find(id="productTitle").get_text().strip()
print(title)

# Set the price below which you would like to get a notification
BUY_PRICE = 90

if price_as_float < BUY_PRICE:
    message = f"{title} is on sale for {price}!"

    # ====================== Send the email ===========================

    with smtplib.SMTP(os.environ["SMTP_ADDRESS"], port=587) as connection:
        connection.starttls()
        result = connection.login(os.environ["EMAIL_ADDRESS"], os.environ["EMAIL_PASSWORD"])
        connection.sendmail(
            from_addr=os.environ["EMAIL_ADDRESS"],
            to_addrs=os.environ["EMAIL_ADDRESS"],
            msg=f"Subject:Amazon Price Alert!\n\n{message}\n{url}".encode("utf-8")
        )

import requests
from bs4 import BeautifulSoup

# This is my user agent.
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36'}

# This is URL of the amazon of what i want to scrape
url = 'https://www.amazon.com/Folgers-Instant-Coffee-Crystals-Classic/dp/B01LB1J9BW/ref=sr_1_1?dchild=1&keywords=instant+coffe&qid=1597498527&sr=8-1'

content = requests.get(url, headers=headers)

s = BeautifulSoup(content.content, 'html.parser')

Product_brand = s.select('#bylineInfo')[0].get_text().strip()
Product_title = s.select('#productTitle')[0].get_text().strip()
Product_price = s.select('#priceblock_ourprice')[0].get_text()
Product_number_of_ratings = s.select('#acrCustomerReviewText')[0].get_text()
Product_ratings = s.select('#acrPopover')[0].get_text()


print(Product_brand)
print(Product_title)
print(Product_price)
print(Product_number_of_ratings)
print(Product_ratings)



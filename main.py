# Anees Busarigit it
# A simple bot that refreshes bestbuy and check for in stock 3000 series GPUs

import bs4
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from fake_useragent import UserAgent 
import time

ua = UserAgent()
opts = Options()
opts.add_argument("user-agent"+ua.random)
driver = webdriver.Chrome(options=opts)


while True:
    # driver.get("https://www.bestbuy.ca/en-ca/collection/graphics-cards-with-nvidia-chipset/349221?path=category%253AComputers%2B%2526%2BTablets%253Bcategory%253APC%2BComponents%253Bcategory%253AGraphics%2BCards%253Bcustom0graphicscardmodel%253AGeForce%2BRTX%2B3060%2BTi%257CGeForce%2BRTX%2B3060")
    driver.get("https://www.bestbuy.ca/en-ca/collection/amd-cpus/347205?icmp=computing_evergreen_cpu_category_listing_category_icon_shopby_amd")
    html = driver.page_source
    soup = bs4.BeautifulSoup(html, "html.parser")
    in_stock = []

    item_in_store = soup.find_all("span",{"class":"container_1DAvI"})

    for product in item_in_store:
        if("Available" in product.text):
            in_stock.append(product.find_parent("a")['href'])

    base_url = "https://www.bestbuy.ca/en-ca"

    for url in in_stock:
        url = base_url + url
        print(url)

    time.sleep(8)

    print("RUN COMPLETE")
import time
from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

options = webdriver.ChromeOptions()
options.add_argument("start-maximized")
url = 'https://www.olx.co.id/jakarta-selatan_g4000030/q-mobil'
driver = webdriver.Chrome()
driver.get(url)

for i in range(10): # ubah ini jika ingin scrape lebih banyak (perhatikan code of conduct guys)
    time.sleep(3) # ubah ini juga 
    try:
        driver.find_element(By.CSS_SELECTOR, 'div._38O09 > button').click()
    except NoSuchElementException:
        break
time.sleep(4)

products=[]
soup =  BeautifulSoup(driver.page_source, 'html.parser')
for item in soup.findAll('li', class_='_1DNjI'):
    product_name = item.find('span', class_='_2poNJ').text
    price = item.find('span', class_='_2Ks63').text
    products.append(
        (product_name, price)
    )

df = pd.DataFrame(products, columns=['Product Name', 'Price'])
df.to_csv('hasil_scrape.csv')
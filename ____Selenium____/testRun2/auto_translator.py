from encodings import utf_8
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

from data import data


website_1 = "https://www.google.com/search?ie=UTF-8&q=google%20translator"

s = Service("C:\webdrivers\chromedriver.exe")
driver = webdriver.Chrome(service=s)
driver.get(website_1)

language = driver.find_element(By.XPATH, '//span[@class="source-language"]')
language.click()

time.sleep(2)
bangla = driver.find_element(
    By.XPATH, '//input[@id="sl_list-search-box"]')
bangla.send_keys("bangla" + Keys.ENTER)


input_text = driver.find_element(
    By.XPATH, '//textarea[@id="tw-source-text-ta"]')

out_csv = []

for d in data:
    input_text.clear()
    input_text.send_keys(d)

    # output_text = driver.find_element(
    #     By.XPATH, '//div[@id="tw-target-text-container"]//span')
    # print("*"*50, output_text.text)
    time.sleep(.7)
    output_text = driver.find_element(
        By.XPATH, '//div[@id="gt-src-is"]//div[@class="gt-is-lb"]/div')
    # By.XPATH, '//div[@id="tw-target-text-container"]//span')

    output_text_value = output_text.text
    print("*"*50, output_text_value)
    out_csv.append(output_text_value)

    time.sleep(1)

for i in out_csv:
    with open("output2.csv", "ab") as file:
        foo = f"\"{i}\",\n"
        file.write(foo.encode('utf-8'))


time.sleep(300)

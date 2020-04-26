# -*- coding: utf-8 -*-
from selenium import webdriver
import datetime
driver = webdriver.Chrome('./chromedriver')
driver.implicitly_wait(1)
driver.get('https://www.alimi.or.kr/api/a/vacant/selectApiVacant.do')
driver.implicitly_wait(1)
table = driver.find_element_by_class_name('search_list')
tbody = table.find_element_by_tag_name("tbody")
rows = tbody.find_elements_by_tag_name("tr")
for index, value in enumerate(rows):
    if(index!=0):
        date=value.find_elements_by_tag_name("td")[1]
        address=value.find_elements_by_tag_name("td")[2]
        print(date.text, address.text)
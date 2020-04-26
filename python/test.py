# -*- coding: utf-8 -*-
from selenium import webdriver
import datetime
driver = webdriver.Chrome('./chromedriver')
driver.implicitly_wait(1)
driver.get('http://www.ewha.ac.kr/mbs/ewhakr/jsp/organizationCon/organizationView.jsp?id=ewhakr_030104010000&cateId=8')
driver.implicitly_wait(1)
table = driver.find_element_by_class_name('tableType01')
tbody = table.find_element_by_tag_name("tbody")
rows = tbody.find_elements_by_tag_name("tr")
for index, value in enumerate(rows):
    if(index!=0):
        title=value.find_elements_by_tag_name("td")
        body=value.find_elements_by_tag_name("p")[1]
        print(body.text)
# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.support.ui import Select
import datetime

driver = webdriver.Chrome('./chromedriver')
driver.implicitly_wait(1)
driver.get('https://www.aia.co.kr/ko/our-products/medical-protection/non-par-denteal-health-plan.html')
driver.implicitly_wait(1)

checkbox = driver.find_element_by_xpath('//*[@id="aia1701849055"]/div/div[1]/div[3]/label/span/span')
name = driver.find_element_by_xpath('//*[@id="aia452730991"]')
birthday = driver.find_element_by_xpath('//*[@id="aia1804180016"]')
sex = driver.find_element_by_xpath('//*[@id="aia1701849055"]/div/div[1]/div[5]/div/div[1]/div/div[2]/div[1]/div[1]')
phoneNumber = driver.find_element_by_xpath('//*[@id="aia1724353200"]')
email = driver.find_element_by_xpath('//*[@id="aia1236626147"]')
prefer = driver.find_element_by_xpath('//*[@id="aia1701849055"]/div/div[1]/div[7]/div/div[1]/div/div[2]/div[1]/div[1]')
button = driver.find_element_by_xpath('//*[@id="btn391303096"]')
button2 = driver.find_element_by_xpath('/html/body/div[12]/section/div/div/div/div/div/div/div[4]/div[1]/div[2]/div/a[2]')

driver.implicitly_wait(3)
checkbox.click()
driver.implicitly_wait(1)
name.send_keys('손민주')
driver.implicitly_wait(1)
birthday.send_keys('19990107')
driver.implicitly_wait(1)
sex.click()
driver.implicitly_wait(1)
phoneNumber.send_keys('01049161954')
driver.implicitly_wait(1)
email.send_keys('tina_98@naver.com')
driver.implicitly_wait(1)
prefer.click()
driver.implicitly_wait(1)
button.click()
driver.implicitly_wait(1)
button2.click()

table = driver.find_element_by_xpath('//*[@id="collapse-large-945472484"]/div[2]/table')
tbody = table.find_element_by_xpath('//*[@id="collapse-large-945472484"]/div[2]/table/tbody')
rows = tbody.find_elements_by_xpath('//*[@id="collapse-large-945472484"]/div[2]/table/tbody/tr')
for index, value in enumerate(rows):
    if(index!=0):
        body=value.find_elements_by_tag_name("td")[1]
        print(body.text)



from selenium import webdriver
import datetime
driver = webdriver.Chrome('./chromedriver')
driver.implicitly_wait(1)
driver.get('https://minjoos.tistory.com/')
driver.implicitly_wait(1)

title = driver.find_element_by_xpath('//*[@id="mArticle"]/div[3]/a/p')
print(title.text)
from selenium import webdriver
import datetime
driver = webdriver.Chrome('./chromedriver')
driver.implicitly_wait(1)
driver.get('http://www.kma.go.kr/info_open/info/open.jsp')
driver.implicitly_wait(1)
table = driver.find_element_by_class_name('table_information')
tbody = table.find_element_by_tag_name("tbody")
rows = tbody.find_elements_by_tag_name("tr")[0]
body= rows.find_elements_by_tag_name("td")
for index, value in enumerate(body):
    print(value.text)
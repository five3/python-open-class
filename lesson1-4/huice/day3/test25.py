from selenium import  webdriver
import re

driver = webdriver.Chrome()
driver.get('http://www.huicewang.com/ecshop')
source = driver.page_source
all_links = re.findall(r'<a.*?/a>',source)

print(len(all_links))

for link in all_links:
    print(link)

driver.quit()


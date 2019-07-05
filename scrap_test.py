import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select




driver = webdriver.Chrome(r'D:\LEWIS\phyton\chromedriver_win32\chromedriver.exe')



driver = driver 
driver.get("https://www.ciudadredonda.org/calendario-lecturas/evangelio-del-dia/?f=2019-07-06")
#assert "YouTube" in driver.title

all_b_element =driver.find_elements_by_tag_name('b')


for bText in all_b_element:
    print('Values b tag: %s',bText)

assert "No results found." not in driver.page_source
  
# driver = driver 
# driver.get("https://www.youtube.com/")
# assert "YouTube" in driver.title
# elem = driver.find_element_by_name("search_query")
# elem.clear()
# elem.send_keys("Linkin Park Castle of glass")
# elem.send_keys(Keys.ENTER)
# assert "No results found." not in driver.page_source
 
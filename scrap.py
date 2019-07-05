import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class PySeargOrg(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(r'D:\LEWIS\phyton\chromedriver_win32\chromedriver.exe')

    def testSearchInPy(self):
        driver = self.driver 
        driver.get("http://www.python.org")
        assert "Python" in driver.title
        elem = driver.find_element_by_name("q")
        elem.clear()
        elem.send_keys("pycon")
        elem.send_keys(Keys.RETURN)
        assert "No results found." not in driver.page_source
    
    
    
    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()
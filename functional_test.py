import time

from selenium import webdriver
import unittest
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

class TestUser(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def test_lista_bairro(self):
        self.browser.get('http://localhost:8000')

        #trajetos = self.browser.find_element_by_id('trajetos')
        trajetos = self.browser.find_element(By.ID,"trajetos")

        self.assertEqual(trajetos.get_attribute('href'),'http://localhost:8000/bairros')

        trajetos.send_keys(Keys.ENTER)
        time.sleep(5)




if __name__ == "__main__":
    unittest.main()

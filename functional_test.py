from importlib import import_module
import time

from selenium import webdriver
import unittest
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

from app_trajeto.models import Bairro


class TestUser(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    
    def test_lista_bairro(self):
        self.browser.get('http://localhost:8000')

        # trajetos = self.browser.find_element_by_id('trajetos')
        trajetos = self.browser.find_element(By.ID,"trajetos")

        self.assertEqual(trajetos.get_attribute('href'),'http://localhost:8000/bairros')

        trajetos.send_keys(Keys.ENTER)
        time.sleep(1)


        pesquisa_bairro = self.browser.find_element(By.ID,"search")
        pesquisa_bairro.send_keys('Aroeira',Keys.ENTER)
       
        time.sleep(1)

        tabela = self.browser.find_element(By.TAG_NAME,"table")
        celulas = tabela.find_elements(By.TAG_NAME,'td')
        self.assertIn('Aroeira', [ celula.text for celula in celulas])
        
        # Bairro.objects.count()

       
        # count_bairros = bairros.objects.count()
        # corpo_tabela = self.browser.find_element(By.TAG_NAME,"tbody")
        # linhas = corpo_tabela.find_elements(By.TAG_NAME,'tr')
        # self.assertEqual(count_bairros, len(linhas) )



if __name__ == "__main__":
    unittest.main(warnings='ignore')

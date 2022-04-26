from django.test import TestCase
from .models import Bairro
# Create your tests here.

class TemplateTest(TestCase):

    def test_inicial(self):
        response = self.client.get('/inicial')
        self.assertTemplateUsed(response, 'app_trajeto/index.html')

    def test_contato(self):
        response = self.client.get('/contato')
        self.assertTemplateUsed(response, 'app_trajeto/contato.html')

    def test_bairro(self):
        response = self.client.get('/bairros')
        self.assertTemplateUsed(response, 'app_trajeto/bairro.html')



    def test_detail_bairro(self):

        response = self.client.get('/detail/&')
        self.assertEqual(response.status_code, 200)


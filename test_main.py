import unittest
import os
from unittest.mock import patch
from flask import Flask, request
from main import hello_http
from dotenv import load_dotenv

load_dotenv()

class TestStarWarsAPI(unittest.TestCase):
    def setUp(self):
        self.app = Flask(__name__)
        self.valid_header = {'x-api-key': os.getenv('API_KEY')}

    def test_auth_failure(self):
        """Testa se a API bloqueia requisições sem a chave de segurança"""
        with self.app.test_request_context('/explore?resource=people'):
            # Passamos o objeto 'request' global do Flask, que contém o contexto atual
            response, status = hello_http(request)
            self.assertEqual(status, 401)

    def test_invalid_resource(self):
        """Testa se a API valida recursos fora da whitelist"""
        with self.app.test_request_context('/explore?resource=jedis', headers=self.valid_header):
            response, status = hello_http(request)
            self.assertEqual(status, 400)

    @patch('main.StarWarsService.fetch_data')
    def test_numeric_sorting(self, mock_fetch):
        """Testa se a ordenação numérica funciona para o diâmetro"""
        mock_fetch.return_value = {
            'results': [
                {'name': 'Bespin', 'diameter': '118000'},
                {'name': 'Naboo', 'diameter': '12120'}
            ]
        }
        with self.app.test_request_context('/explore?resource=planets&sort_by=diameter', headers=self.valid_header):
            response, status = hello_http(request)
            data = response.get_json()
            # Naboo (12120) deve vir antes de Bespin (118000) na ordenação numérica
            self.assertEqual(data['data'][0]['name'], 'Naboo')

if __name__ == '__main__':
    unittest.main()
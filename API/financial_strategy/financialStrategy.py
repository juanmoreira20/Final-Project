import unittest

import requests
import os
import sys

current_dir = os.path.dirname(os.path.realpath(__file__))
path_dir = os.path.join(current_dir, 'features/steps/json_scenarios')
sys.path.append(path_dir)

from json_utils import *

class companies(unittest.TestCase):
    def setUp(self):
        self.url = get_url()

    def test_1_get_companies(self):

        company_id = get_id()
        auth = get_token()

        header = {'authorization': auth}
        response = requests.get(f'{self.url}/financial-strategy/{company_id}', headers=header)
        assert response.status_code

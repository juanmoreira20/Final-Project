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
        response = requests.get(f'{self.url}/dashboard/goals/{company_id}', headers=header)
        assert response.status_code == 200

        json_data = json.loads(response.text)
        i = 0
        for item in json_data:
            if i == 0:
                self.assertIn('breakevenPoint', item)
                self.assertEqual(type(json_data[item]), float)
                i = i + 1
            elif i == 1:
                self.assertIn(('salesGoal'), item)
                self.assertEqual(type(json_data[item]), float)
                i = i + 1
            elif i == 2:
                self.assertIn(('totalTaxForSale'), item)
                self.assertEqual(type(json_data[item]), float)
                i = i+1
            elif i == 3:
                self.assertIn(('unitBP'), item)
                self.assertEqual(type(json_data[item]), float)
                i = i +1

            else:
                self.assertIn(('unitSG'), item)
                self.assertEqual(type(json_data[item]), float)
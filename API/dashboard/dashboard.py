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
        response = requests.get(f'{self.url}/dashboard/{company_id}', headers=header)
        assert response.status_code == 200

        json_data = json.loads(response.text)
        i = 0
        for item in json_data:
            if i == 0:
                self.assertIn('journeys', item)
                self.assertEqual(type(json_data[item]), list)
                i = i + 1
            elif i == 1:
                self.assertIn(('goals'), item)
                self.assertEqual(type(json_data[item]), dict)
                i = i + 1
            elif i == 2:
                self.assertIn(('progress'), item)
                self.assertEqual(type(json_data[item]), dict)
                i = i+1
            elif i == 3:
                self.assertIn(('saleDevolutionInfo'), item)
                self.assertEqual(type(json_data[item]), dict)
                i = i +1
            elif i == 4:
                self.assertIn(('totalProductsSelled'), item)
                self.assertEqual(type(json_data[item]), float)
                i = i +1
            elif i == 5:
                self.assertIn(('percentAveragePresence'), item)
                self.assertEqual(type(json_data[item]), float)
                i = i +1
            elif i == 6:
                self.assertIn(('formulas'), item)
                self.assertEqual(type(json_data[item]), dict)
                i = i +1
            elif i == 7:
                self.assertIn(('dre1'), item)
                self.assertEqual(type(json_data[item]), dict)
                i = i +1
            else:
                self.assertIn(('dre2'), item)
                self.assertEqual(type(json_data[item]), dict)
import unittest
from http import HTTPStatus
import requests
import json


class TestCallAPI(unittest.TestCase):
    def test_add_new_call(self):
        payload = json.dumps({"call_duration": 3000})
        user_name = 'Vin'
        url = "http://127.0.0.1:6868/mobile/{}/call".format(user_name)
        headers = {
            'Content-Type': 'application/json'
        }
        response = requests.request("PUT", url, headers=headers, data=payload)
        self.assertEqual(response.status_code, HTTPStatus.OK)

    def test_add_new_call_with_invalid_username(self):
        payload = json.dumps({"call_duration": 3000})
        user_name = 'Vin' * 30
        url = "http://127.0.0.1:6868/mobile/{}/call".format(user_name)
        headers = {
            'Content-Type': 'application/json'
        }
        response = requests.request("PUT", url, headers=headers, data=payload)
        self.assertEqual(response.status_code, HTTPStatus.BAD_REQUEST)

    def test_add_new_call_with_invalid_call_duration(self):
        payload = json.dumps({"call_duration": -99999})
        user_name = 'Vin'
        url = "http://127.0.0.1:6868/mobile/{}/call".format(user_name)
        headers = {
            'Content-Type': 'application/json'
        }
        response = requests.request("PUT", url, headers=headers, data=payload)
        self.assertEqual(response.status_code, HTTPStatus.BAD_REQUEST)


class TestBillingAPI(unittest.TestCase):
    def test_get_billing(self):
        user_name = 'Vin'
        url = "http://127.0.0.1:6868/mobile/{}/billing".format(user_name)
        response = requests.request("GET", url, headers={}, data={})
        self.assertEqual(response.status_code, HTTPStatus.OK)

    def test_get_billing_with_not_found_username(self):
        user_name = 'VinBigData'
        url = "http://127.0.0.1:6868/mobile/{}/billing".format(user_name)
        response = requests.request("GET", url, headers={}, data={})
        self.assertEqual(response.status_code, HTTPStatus.BAD_REQUEST)


if __name__ == '__main__':
    unittest.main(verbosity=2)

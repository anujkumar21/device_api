import logging
import unittest

import requests

from utilities.services import Services

logging.basicConfig(format='%(asctime)s - %(levelname)s: %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p',
                    level=logging.INFO)


class BaseTest(unittest.TestCase):
    """
    This class is to write test cases related to public APIs on https://reqres.in/
    """

    def setUp(self):
        self.url = "http://localhost:8080/"
        self.headers = {'Content-type': 'application/json'}
        self.services = Services()

    def tearDown(self):
        requests.post(self.url + "disconnect", headers=self.headers)


if __name__ == '__main__':
    unittest.main()

import json
import logging

import requests

from base.base_test import BaseTest


class TestDisconnect(BaseTest):
    """
    This class is to test POST API to disconnect devices.
    """

    def test_disconnect(self):
        """
        Verify user should be able to disconnect devices.
        """
        url = self.url + "disconnect"
        logging.info("# POST url: " + url)

        response = requests.post(url, headers=self.headers)
        actual_status_code = response.status_code
        json_response = json.loads(response.text)

        logging.info("# Actual response code: " + str(actual_status_code))
        assert actual_status_code == 200, "status code {0} should be 200.".format(actual_status_code)
        assert json_response['success'], "success should be True"

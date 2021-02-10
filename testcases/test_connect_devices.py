import json
import logging

import requests

from base.base_test import BaseTest


class TestConnectDevices(BaseTest):
    """
    This class is to test POST API to connect devices.
    """

    def test_connect(self, ip="192.168.100.10"):
        """
        Verify user should be able to connect devices using POST API.
        """
        url = self.url + "connect"
        logging.info("# POST url: " + url)

        response = requests.post(url, data=self.services.get_request_body(ip), headers=self.headers)
        actual_status_code = response.status_code
        json_response = json.loads(response.text)

        logging.info("# Actual response code: " + str(actual_status_code))
        assert actual_status_code == 200, "status code {0} should be 200.".format(actual_status_code)
        assert json_response['success'], "success should be True, but was " + str(json_response['success'])

    def test_connect_with_invalid_ip(self, ip="invalid.ip"):
        """
        Verify POST API should return success as False for invalid ip.
        """
        url = self.url + "connect"
        logging.info("# POST url: " + url)

        response = requests.post(url, data=self.services.get_request_body(ip), headers=self.headers)
        actual_status_code = response.status_code
        json_response = json.loads(response.text)

        logging.info("# Actual response code: " + str(actual_status_code))
        assert actual_status_code == 200, "status code {0} should be 200.".format(actual_status_code)
        assert not json_response['success'], "success should be False, but was " + str(json_response['success'])

    def test_connect_with_get_request_type(self):
        """
        Verify user should not be able to send connect POST API as GET request.
        """
        url = self.url + "connect"
        logging.info("# POST url: " + url)

        response = requests.get(url, headers=self.headers)
        actual_status_code = response.status_code

        logging.info("# Actual response code: " + str(actual_status_code))
        assert actual_status_code == 405, "status code {0} should be 405 Method Not Allowed.".format(actual_status_code)

    def test_single_device_connected(self):
        """
        Verify user should be able to connect one device at a time.
        """
        url = self.url + "connect"
        logging.info("# POST url: " + url)

        requests.post(url, data=self.services.get_request_body("192.168.100.10"), headers=self.headers)

        response = requests.post(url, data=self.services.get_request_body("192.168.100.11"),
                                 headers=self.headers)

        actual_status_code = response.status_code
        logging.info("# Actual response code: " + str(actual_status_code))
        assert actual_status_code == 200, "status code {0} should be 200.".format(actual_status_code)

        assert not json.loads(response.text)['success'], \
            "success status should be False, if user connects more than one device."

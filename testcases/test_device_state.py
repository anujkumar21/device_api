import json
import logging

import requests

from base.base_test import BaseTest


class TestDeviceState(BaseTest):
    """
    This class is to test GET API to get device state.
    """

    def test_device_state(self):
        """
        Verify user should be able to validate device state.
        """
        self.prerequisite()
        url = self.url + "state"
        logging.info("# GET device state endpoint: " + url)

        response = requests.get(url)
        actual_status_code = response.status_code
        logging.info("# Actual response code: " + str(actual_status_code))
        assert actual_status_code == 200, "status code {0} should be 200.".format(actual_status_code)

        expected_response = self.services.get_expected_response("device-state")
        assert json.loads(response.text) == expected_response, "State should be {0}, but was {1}".format(
            expected_response, response.text)

    def test_no_device_connected_state(self):
        """
        Verify success status is False when no device is connected.
        """
        url = self.url + "state"
        logging.info("# GET device state endpoint: " + url)

        response = requests.get(url)
        actual_status_code = response.status_code
        logging.info("# Actual response code: " + str(actual_status_code))
        assert actual_status_code == 200, "status code {0} should be 200.".format(actual_status_code)

        assert not json.loads(response.text)['success'], "success status should be False, when no device is connected."

    def prerequisite(self, ip="192.168.100.10"):
        url = self.url + "connect"
        body = self.services.get_request_body(ip)
        requests.post(url, data=json.dumps(body), headers=self.headers)
        logging.info("# Device {} has been connected.".format(ip))

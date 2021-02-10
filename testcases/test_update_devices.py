import json
import logging

import requests
from parameterized import parameterized

from base.base_test import BaseTest


class TestUpdateDevices(BaseTest):
    """
    This class is to test POST API to update device properties.
    """

    @parameterized.expand([
        ("name", "automation"),
        ("color", "#9FE2BF"),
        ("brightness", "5.0")
    ])
    def test_update_device(self, key, value):
        """
        Verify user should be able to update device properties.
        """
        self.prerequisite()
        url = self.url + key
        logging.info("# POST url: " + url)

        body = self.services.get_request_body(value, "update." + key)
        response = requests.post(url, data=body, headers=self.headers)
        actual_status_code = response.status_code
        json_response = json.loads(response.text)

        logging.info("# Actual response code: " + str(actual_status_code))
        assert actual_status_code == 200, "status code {0} should be 200.".format(actual_status_code)
        assert json_response["success"], "success should be True."

        url = self.url + "state"
        logging.info("# GET device state endpoint: " + url)

        response = json.loads(requests.get(url).text)
        if key == 'brightness':
            value = float(value)
            response[key] = float(response[key])

        assert response[key] == value, "{0} should be {1}, but was {1}".format(key, value, response[key])

    def test_update_device_ip(self):
        """
        Verify user should be able to update device properties.
        """
        self.prerequisite()
        url = self.url + "ip"
        logging.info("# POST url: " + url)

        body = self.services.get_request_body("192.168.100.15", "update." + "ip")
        response = requests.post(url, data=body, headers=self.headers)
        actual_status_code = response.status_code
        logging.info("# Actual response code: " + str(actual_status_code))
        assert actual_status_code == 404, "status code {0} should be 200.".format(actual_status_code)

    def prerequisite(self, ip="192.168.100.10"):
        url = self.url + "connect"
        body = self.services.get_request_body(ip)
        requests.post(url, data=json.dumps(body), headers=self.headers)
        logging.info("# Device {} has been connected.".format(ip))

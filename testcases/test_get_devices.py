import json
import logging

import requests

from base.base_test import BaseTest


class GetDevicesTest(BaseTest):
    """
    This class is to test GET API to get all devices.
    """

    def test_get_devices(self):
        """
        Verify GET request to get all devices.
        """
        url = self.url + "devices"
        logging.info("# GET devices url: " + url)

        response = requests.get(url)
        actual_status_code = response.status_code
        logging.info("# Actual response code: " + str(actual_status_code))
        assert actual_status_code == 200, "status code {0} should be 200.".format(actual_status_code)

        devices = json.loads(response.text)
        logging.info("# Actual devices: " + str(devices))
        for device in devices:
            actual_ip = device['ip']
            assert str(self.services.is_valid_ip_address(actual_ip)), actual_ip + " should be ipv4 format."

    def test_get_devices_with_invalid_path(self):
        """
        Verify GET request path.
        """
        url = self.url + "dev"
        logging.info("# GET devices url: " + url)

        response = requests.get(url)
        actual_status_code = response.status_code
        logging.info("# Actual response code: " + str(actual_status_code))
        assert actual_status_code == 404, "status code {0} should be 400.".format(actual_status_code)

import json

from configparser import ConfigParser
from pathlib import Path


class Services:
    """
    This class is for maintaining the utilities related to json objects
    """

    def __init__(self):
        self.config = ConfigParser()
        self.test_data = str(Path(__file__).parent.parent) + "/resources/test_data.ini"

    def get_request_body(self, value, req="post"):
        """
        This method is to get json body from resources folder
        :return: json body
        """

        self.config.read(self.test_data)
        request_body = json.loads(self.config.get("request", req))
        for key in request_body:
            request_body[key] = value
        return request_body

    def get_expected_response(self, key):
        """
        This method is to get json body from resources folder
        :return: json body
        """
        self.config.read(self.test_data)
        response_body = json.loads(self.config.get("response", key))
        for pair in self.config.items("device1"):
            if pair[0] == "brightness":
                response_body[pair[0]] = float(pair[1])
            else:
                response_body[pair[0]] = pair[1]
        return response_body

    def is_valid_ip_address(self, ip):
        return ip.count(".") == 3 and all(str(int(i)) == i and 0 <= int(i) <= 255 for i in ip.split("."))

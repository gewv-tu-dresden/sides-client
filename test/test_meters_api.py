"""
    The api of the tek ekg boxes and field controller.

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by: https://openapi-generator.tech
"""


import unittest

import gewv_sides_client
from gewv_sides_client.api.meters_api import MetersApi  # noqa: E501


class TestMetersApi(unittest.TestCase):
    """MetersApi unit test stubs"""

    def setUp(self):
        self.api = MetersApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_create_reading(self):
        """Test case for create_reading

        """
        pass

    def test_delete_reading(self):
        """Test case for delete_reading

        """
        pass

    def test_get_readings(self):
        """Test case for get_readings

        """
        pass

    def test_upsert_reading(self):
        """Test case for upsert_reading

        """
        pass


if __name__ == '__main__':
    unittest.main()

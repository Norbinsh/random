"""
Single TestCase to test some of the module's basic methods
"""

import unittest
from shutil import rmtree
import sys
sys.path.append('..')
import actual.WebDriverSetup as WebDriverSetup

class TestOsLevelPrep(unittest.TestCase):
    """
    A simple test case example to try and catch possibly network or IO errors related to obtaining the WebDriver
    """

    def setUp(self):
        self.x = WebDriverSetup.OsLevelPrep('chrome')

    def test_expected_driver_binary_name(self):
        """
        Checks if one of the expected values returned
        """
        result = self.x.expected_driver_binary_name()
        self.assertTrue(result in ['chromedriver', 'chromedriver.exe', 'ff'])

    def test_check_driver_exists(self):
        """
        Checks if the driver's file exists and return bool
        """
        result = self.x.check_driver_exists()
        self.assertTrue(result)

    def test_obtain_driver_binary(self):
        """
        See if the zip file download and extraction was successful
        """
        result = self.x.obtain_driver_binary()
        rmtree(self.x.driver_dir)
        print("Deleted test driver dir")
        self.assertTrue(result)

if __name__ == '__main__':
    unittest.main()

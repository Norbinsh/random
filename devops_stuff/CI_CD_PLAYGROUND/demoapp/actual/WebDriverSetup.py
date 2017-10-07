"""
This example module will take care of the process for obtaining the ChromeDriver and verifying it is ready to use.
"""

import os
import sys
import urllib.request
from zipfile import ZipFile
from io import BytesIO


class OsLevelPrep:
    """
    Obtain the needed WebDriver for the specific Operating System / Architecture
    """
    def __init__(self, client_application):
        self.client_application = client_application
        self.operating_system = self.which_os()
        self.driver_dir = 'WebDriver'
        self.posix_64_url = 'https://chromedriver.storage.googleapis.com/2.30/chromedriver_linux64.zip'
        self.posix_32_url = 'https://chromedriver.storage.googleapis.com/2.30/chromedriver_linux32.zip'
        self.nt_url = 'https://chromedriver.storage.googleapis.com/2.30/chromedriver_win32.zip'
        self.driver_name = self.expected_driver_binary_name()
        self.__client_application = None
        self.active_url = None
        self.runner = self.runner()

    @property
    def client_application(self) -> object:
        """
        Access/Get the 'client_application' property, for validation
        """
        return self.__client_application

    @client_application.setter
    def client_application(self, clapp_value: str):
        """
        Validate either chrome or firefox are provided as client applications.
        """
        if clapp_value.lower() != 'chrome' and clapp_value.lower() != 'firefox':
            raise ValueError("Only 'chrome' and 'firefox' are supported")
        self.__client_application = clapp_value

    def check_driver_exists(self) -> bool:
        """
        Check inside the package's 'WebDriver' directory to see if the driver already exists for the
        given operating system & client application combination.
        """
        return True if self.expected_driver_binary_name() == 'ff' else \
            os.path.isfile('{driver_dir}/{bin_name}'.format(driver_dir=self.driver_dir,
                                                            bin_name=self.expected_driver_binary_name()))

    def expected_driver_binary_name(self) -> str:
        """
        Returns the expected WebDriver binary file name (For Chrome's mainly, as Firefox comes built in with
        Selenium).
        """
        _os_vals = self.which_os()
        if self.client_application == 'firefox':
            return 'ff'
        else:
            if _os_vals[0] == 'posix':
                self.active_url = self.posix_64_url if _os_vals[1] else self.posix_32_url
                return 'chromedriver'
            elif _os_vals[0] == 'nt':
                self.active_url = self.nt_url
                return 'chromedriver.exe'
            else:
                return "unsupported os"

    def obtain_driver_binary(self):
        """
        Download the zip file, and extract into the driver directory.
        """
        if self.active_url:
            url = self.active_url
            with urllib.request.urlopen(url) as zf:
                with ZipFile(BytesIO(zf.read())) as df:
                    df.extractall(self.driver_dir)
                    return True
        else:
            return False

    def runner(self):
        """
        Call the relevant instance methods.
        """
        if not self.check_driver_exists():
            self.obtain_driver_binary()

    @staticmethod
    def which_os() -> tuple:
        """
        Returns a tuple describing the operating system the scripts runs on and its architecture.
        """
        return os.name, sys.maxsize > 2**32


if __name__ == '__main__':
    """
    Create an instance of OsLevelPrep and start the OS prep/checks.
    """
    OsLevelPrep('chrome')


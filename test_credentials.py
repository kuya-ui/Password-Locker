import unittest
from credentials import Credential
class TestCredential(unittest.TestCase):

    """
    Test class that defines test cases for the credential class behaviours,
    the arguments help in creating test cases.
    """

    def setUp(self):

        """
        this method runs before each test case, carries the instructions of what is to be done
        """

        self.new_password = Credential("max")
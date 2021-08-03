import unittest
from user import User

class TestUser(unittest.TestCase):

    '''
    Test class that defines test cases for the contact class behaviours.
    '''

def setUp(self):
    '''
    Set up method to run before each test cases.
    '''

    def tearDown(self):

        """
        tearDown method does clean up after each test case has runself.
        """

    self.new_user = User("facebook","millan","abcd","abcd")

def test_init(self):
    '''
    test_init test case to test if the object is initialized properly
    '''

    self.assertEqual(self.new_user.account-name, "facebook")
    self.assertEqual(self.new_user.username,"millan")
    self.assertEqual(self.new_user.password,"abcd")
    self.assertEqual(self.new_user.confirm_password,"abcd")
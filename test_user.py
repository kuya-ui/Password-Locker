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


def test_save_detail(self):
       """
        the test_save_detail test is used to test if the contact object is saved into details
        """
       self.new_user.save_detail()

       self.assertEqual(len(User.user_detail),1)

def test_save_multiple_detail(self):

        """
        a method to check if we can save multiple user details to our details array
        """
def test_display_all_details():

        """
        is a method that returns a list of all details saved
        """

        self.assertEqual(User.display_all_details(),User.user_detail)

if __name__ == '__main__':
    unittest.main()
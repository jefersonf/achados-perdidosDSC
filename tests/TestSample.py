import unittest
import sys

sys.path.append('../../')
sys.path.append('../')

class TestSample(unittest.TestCase):

    def setUp(self):

        # TO DO
        pass

    def test_constructor(self):

        # TO DO
        pass

        ''' 
        # exemplos de assertions 
        user = User('User', 'user@gmail.com', '(83)91234-56789', '114110478', '123456789')

        self.assertEqual(user.getName(), 'User')
        self.assertEqual(user.getEmail(), 'user@gmail.com')
        self.assertEqual(user.getPhone(), '(83)91234-56789')
        self.assertEqual(user.getPassword(), '123456789')

        user = User('User', 'user3@gmail.com', '(83)91234-56789', '114110478')

        self.assertTrue(user.getPassword() != None)
        '''

if __name__ == '__main__':
    unittest.main()

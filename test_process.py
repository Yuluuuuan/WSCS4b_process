from process import create_train_dateset
from process import create_test_dateset
import unittest

class TestStringMethods(unittest.TestCase):
    # local testing
    def test_visualization(self):
        self.assertEqual(create_train_dateset('data'),'/data/trainset.csv')
        self.assertEqual(create_test_dateset('data'),'/data/testset.csv')
if __name__=="__main__":
    unittest.main()
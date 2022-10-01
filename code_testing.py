import unittest
from worksheet import create_new_account


class TestWorksheet(unittest.TestCase):
    """
    Testing on worksheet.py file
    """
    def test_create_new_account_succ(self):
        """
        Test create_new_account funtion equal
        """
        result = create_new_account("raz", 1234)
        self.assertEqual(result, ["raz", 1234, 0])

    def test_create_new_account_fail(self):
        """
        Test create_new_acount function not equal
        """
        result = create_new_account("raz", "1234")
        self.assertNotEqual(result, ("raz", "1234", 0))


if __name__ == "__main__":
    unittest.main()

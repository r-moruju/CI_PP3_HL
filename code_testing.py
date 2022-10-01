import unittest
from worksheet import create_new_account
from worksheet import height_scores
from countries_api import country_class
from countries_api import Country


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

    def test_height_scores(self):
        self.assertEqual(height_scores()["Test1"], "0")


class TestCountriesApi(unittest.TestCase):
    """
    Tests on country_api.py file
    """
    def test_country_class_equal(self):
        """
        Test country_class function
        """
        country1 = "Nepal"
        country1_population = 29136808
        self.assertEqual(country_class(country1), country1_population)
        country2 = "Afghanistan"
        country2_population = 38928346
        self.assertEqual(country_class(country2), country2_population)

    def test_country_class_not_equal(self):
        """
        Test country_class function
        """
        country1 = "Nepal"
        country1_population = 29136807
        self.assertNotEqual(country_class(country1), country1_population)
        country2 = "Afghanistan"
        country2_population = 28928346
        self.assertNotEqual(country_class(country2), country2_population)

    def test_country_class(self):
        """
        Test the Country class
        """
        country = Country("Romania", 19000000)
        self.assertEqual(country.population, 19000000)
        self.assertEqual(country.name, "Romania")


if __name__ == "__main__":
    unittest.main()

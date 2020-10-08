from city_functions import format_places
import unittest

class CityTestCase(unittest.TestCase):

    def test_city_country(self):
        formatted = format_places("Fort Wayne", "USA")
        self.assertEqual(formatted, "Fort Wayne, USA")


if __name__ == '__main__':
    unittest.main()

else:
    ctc = CityTestCase()
    ctc.test_city_country()


from city_functions2 import format_places, format_places_optional
import unittest


class CityTestCase(unittest.TestCase):

    def test_city_country(self):
        formatted = format_places("Fort Wayne", "USA", 4000)
        self.assertEqual(formatted, "Fort Wayne, USA - 4000")

    def test_city_country_population(self):
        formatted = format_places_optional(city_name="Fort Wayne", country_name="USA")
        self.assertEqual(formatted, "Fort Wayne, USA")

    def test_city_country_population_2(self):
        formatted = format_places_optional(city_name="Fort Wayne", country_name="USA", population=3000)
        self.assertEqual(formatted, "Fort Wayne, USA - 3000")

if __name__ == '__main__':
    unittest.main()

else:
    ctc = CityTestCase()



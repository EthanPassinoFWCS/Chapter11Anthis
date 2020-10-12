from TIY11_3 import *
import unittest


class EmployeeTestCase(unittest.TestCase):
    def setUp(self):
        self.employee = Employee("Ethan", "Passino", 98000)

    def test_give_default_raise(self):
        self.employee.give_raise()
        self.assertEqual(self.employee.annual_salary, 98000+5000)

    def test_give_custom_raise(self):
        self.employee.give_raise(13000)
        self.assertEqual(self.employee.annual_salary, 98000+13000)


if __name__ == '__main__':
    unittest.main()





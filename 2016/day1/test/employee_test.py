#!/usr/bin/env python3
import unittest
import datetime
import examples.tdd.version05.employee as employee

class TestEmployee(unittest.TestCase):

    def test_employee_object_creation(self):
        emp = employee.Employee("Karen", "Jones", "Manager",
                                datetime.date.today())

    def test_get_employee_properties(self):
        emp = employee.Employee("Karen", "Jones", "Manager",
                                datetime.date.today())
        self.assertEqual(emp.first_name, "Karen")
        self.assertEqual(emp.last_name, "Jones")
        self.assertEqual(emp.job, "Manager")
        self.assertEqual(emp.hired, datetime.date.today())

if __name__ == "__main__":
    unittest.main()
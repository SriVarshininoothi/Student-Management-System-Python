import sys
import os

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import unittest
from models import Student
class TestStudent(unittest.TestCase):

    def setUp(self):
        self.student = Student(
            101,
            "Rahul",
            21,
            "Python",
            "rahul@gmail.com"
        )

    def test_student_creation(self):
        self.assertEqual(self.student.get_student_id(), 101)
        self.assertEqual(self.student.get_name(), "Rahul")

    def test_set_name(self):
        result = self.student.set_name("Arun")
        self.assertTrue(result)
        self.assertEqual(self.student.get_name(), "Arun")

    def test_mark_attendance(self):
        result = self.student.set_attendance(
            "2026-11-17", "Present"
        )
        self.assertTrue(result)

    def test_duplicate_attendance(self):
        self.student.set_attendance(
            "2026-11-17", "Present"
        )

        result = self.student.set_attendance(
            "2026-11-17", "Absent"
        )

        self.assertFalse(result)

    def test_invalid_name(self):
        result = self.student.set_name("")
        self.assertFalse(result)


    def test_invalid_age(self):
        result = self.student.set_age(-5)
        self.assertFalse(result)


    def test_invalid_email(self):
        result = self.student.set_email("invalidemail")
        self.assertFalse(result)


    def test_invalid_attendance_status(self):
        result = self.student.set_attendance(
            "2026-11-18", "Holiday"
        )
        self.assertFalse(result)


if __name__ == "__main__":
    unittest.main()
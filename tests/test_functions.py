
import functions as student_functions
from models import Student

import pytest


# Fixture to create isolated student data for every test

@pytest.fixture
def setup_students(monkeypatch):

    test_students = [
        Student(101, "Rahul", 21, "Python", "rahul@gmail.com")
    ]

    monkeypatch.setattr(student_functions, "students", test_students)

    # Prevent tests from modifying actual JSON data
    monkeypatch.setattr(
        student_functions,
        "save_students",
        lambda students: None
    )

    return test_students


# 1. Find Student

def test_find_student(setup_students):

    student = student_functions.find_student(101)

    assert student is not None
    assert student.get_name() == "Rahul"


def test_find_non_existing_student(setup_students):

    student = student_functions.find_student(999)

    assert student is None


# 2. Add Student

def test_add_student(monkeypatch, setup_students):

    inputs = iter([
        "102",
        "Arjun",
        "22",
        "Java",
        "arjun@gmail.com"
    ])

    monkeypatch.setattr("builtins.input", lambda _: next(inputs))

    student_functions.add_student()

    assert len(setup_students) == 2
    assert student_functions.find_student(102).get_name() == "Arjun"


def test_add_duplicate_student(monkeypatch, setup_students):

    inputs = iter(["101"])

    monkeypatch.setattr("builtins.input", lambda _: next(inputs))

    student_functions.add_student()

    assert len(setup_students) == 1


# 3. Search Student

def test_search_student(monkeypatch, setup_students, capsys):

    monkeypatch.setattr("builtins.input", lambda _: "101")

    student_functions.search_student()

    output = capsys.readouterr().out

    assert "Student Found!" in output
    assert "Rahul" in output


# 4. Update Student

def test_update_student(monkeypatch, setup_students):

    inputs = iter([
        "101",       # Student ID
        "yes",       # Update name
        "Arjun",     # New name
        "no",        # Update age
        "no",        # Update course
        "no"         # Update email
    ])

    monkeypatch.setattr("builtins.input", lambda _: next(inputs))

    student_functions.update_student()

    assert student_functions.find_student(101).get_name() == "Arjun"


# 5. Delete Student

def test_delete_student(monkeypatch, setup_students):

    inputs = iter([
        "101",
        "yes"
    ])

    monkeypatch.setattr("builtins.input", lambda _: next(inputs))

    student_functions.delete_student()

    assert len(setup_students) == 0
    assert student_functions.find_student(101) is None


# 6. Add Marks

def test_add_marks(monkeypatch, setup_students):

    inputs = iter([
        "101",
        "Python",
        "90"
    ])

    monkeypatch.setattr("builtins.input", lambda _: next(inputs))

    student_functions.add_marks()

    assert setup_students[0].get_marks()["Python"] == 90


# 7. Mark Attendance

def test_mark_attendance(monkeypatch, setup_students):

    inputs = iter([
        "101",
        "2026-11-18",
        "Present"
    ])

    monkeypatch.setattr("builtins.input", lambda _: next(inputs))

    student_functions.mark_attendance()

    assert setup_students[0].get_attendance()["2026-11-18"] == "Present"

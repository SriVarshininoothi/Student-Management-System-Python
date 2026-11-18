
from validation import (
    validate_student_id,
    validate_name,
    validate_email,
    validate_age,
    validate_course,
    validate_marks,
    validate_attendance
)


# Student ID validation

def test_valid_student_id():
    assert validate_student_id(101) is True


def test_invalid_student_id():
    assert validate_student_id(-1) is False


# Name validation

def test_valid_name():
    assert validate_name("Rahul") is True


def test_invalid_name():
    assert validate_name("") is False


# Email validation

def test_valid_email():
    assert validate_email("rahul@gmail.com") is True


def test_invalid_email():
    assert validate_email("invalidemail") is False


# Age validation

def test_valid_age():
    assert validate_age(21) is True


def test_invalid_age():
    assert validate_age(-5) is False


# Course validation

def test_valid_course():
    assert validate_course("Python") is True


def test_invalid_course():
    assert validate_course("") is False


# Marks validation

def test_valid_marks():
    assert validate_marks(90) is True


def test_invalid_marks():
    assert validate_marks(110) is False

# Attendance Validation

def test_valid_attendance():
    assert validate_attendance("Present") is True


def test_absent_attendance():
    assert validate_attendance("Absent") is True


def test_invalid_attendance():
    assert validate_attendance("Holiday") is False


def test_empty_attendance():
    assert validate_attendance("") is False
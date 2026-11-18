
import json
import os
import storage
import pytest

from models import Student


# Fixture to use a temporary directory for JSON storage

@pytest.fixture
def temp_storage(tmp_path, monkeypatch):

    monkeypatch.chdir(tmp_path)

    return tmp_path


# Create sample student

def create_student():

    student = Student(
        101,
        "Rahul",
        21,
        "Python",
        "rahul@gmail.com"
    )

    student.set_marks("Python", 90)
    student.set_marks("SQL", 85)

    student.set_attendance("2026-11-17", "Present")
    student.set_attendance("2026-11-18", "Absent")

    return student


# 1. Test saving students

def test_save_students(temp_storage):

    students = [create_student()]

    storage.save_students(students)

    file_path = temp_storage / "data" / "students.json"

    assert file_path.exists()

    with open(file_path, "r") as file:
        data = json.load(file)

    assert len(data) == 1
    assert data[0]["student_id"] == 101
    assert data[0]["name"] == "Rahul"


# 2. Test loading students

def test_load_students(temp_storage):

    students = [create_student()]

    storage.save_students(students)

    loaded_students = storage.load_students()

    assert len(loaded_students) == 1
    assert loaded_students[0].get_student_id() == 101
    assert loaded_students[0].get_name() == "Rahul"


# 3. Test marks persistence

def test_marks_persistence(temp_storage):

    students = [create_student()]

    storage.save_students(students)

    loaded_students = storage.load_students()

    marks = loaded_students[0].get_marks()

    assert marks["Python"] == 90
    assert marks["SQL"] == 85


# 4. Test attendance persistence

def test_attendance_persistence(temp_storage):

    students = [create_student()]

    storage.save_students(students)

    loaded_students = storage.load_students()

    attendance = loaded_students[0].get_attendance()

    assert attendance["2026-11-17"] == "Present"
    assert attendance["2026-11-18"] == "Absent"


# 5. Test saving empty student list

def test_save_empty_students(temp_storage):

    storage.save_students([])

    loaded_students = storage.load_students()

    assert loaded_students == []


# 6. Test loading when JSON file does not exist

def test_load_missing_file(temp_storage):

    loaded_students = storage.load_students()

    assert loaded_students == []


# 7. Test loading invalid JSON

def test_load_invalid_json(temp_storage, capsys):

    os.makedirs("data", exist_ok=True)

    with open("data/students.json", "w") as file:
        file.write("invalid json")

    loaded_students = storage.load_students()

    output = capsys.readouterr().out

    assert loaded_students == []
    assert "Invalid or empty JSON file" in output


import pytest
import reports
import functions

from models import Student


@pytest.fixture
def setup_student(monkeypatch):

    student = Student(
        101,
        "Rahul",
        21,
        "Python",
        "rahul@gmail.com"
    )

    student.set_marks("Python", 90)
    student.set_marks("SQL", 80)

    student.set_attendance("2026-11-17", "Present")
    student.set_attendance("2026-11-18", "Absent")

    students = [student]

    monkeypatch.setattr(functions, "students", students)

    return student


# 1. Generate Student Report

def test_generate_student_report(monkeypatch, setup_student, capsys):

    monkeypatch.setattr("builtins.input", lambda _: "101")

    reports.generate_student_report()

    output = capsys.readouterr().out

    assert "Rahul" in output
    assert "Python" in output
    assert "Total Marks" in output
    assert "Average" in output
    assert "Pass" in output


# 2. View Attendance

def test_view_attendance(monkeypatch, setup_student, capsys):

    monkeypatch.setattr("builtins.input", lambda _: "101")

    reports.view_attendance()

    output = capsys.readouterr().out

    assert "Rahul" in output
    assert "2026-11-17" in output
    assert "Present" in output
    assert "Absent" in output

def test_calculate_attendance_percentage(
    monkeypatch, setup_student, capsys
):

    monkeypatch.setattr("builtins.input", lambda _: "101")

    reports.calculate_attendance_percentage()

    output = capsys.readouterr().out

    assert "Present Days" in output
    assert "Absent Days" in output
    assert "Total Days" in output
    assert "50.00%" in output
    
# 4. Student Without Marks

def test_report_without_marks(monkeypatch, setup_student, capsys):

    setup_student.get_marks().clear()

    monkeypatch.setattr("builtins.input", lambda _: "101")

    reports.generate_student_report()

    output = capsys.readouterr().out

    assert "No marks available" in output


# 5. Student Without Attendance

def test_view_attendance_without_records(
    monkeypatch, setup_student, capsys
):

    setup_student.get_attendance().clear()

    monkeypatch.setattr("builtins.input", lambda _: "101")

    reports.view_attendance()

    output = capsys.readouterr().out

    assert "No attendance records found" in output


# 6. Student Not Found

def test_report_student_not_found(monkeypatch, setup_student, capsys):

    monkeypatch.setattr("builtins.input", lambda _: "999")

    reports.generate_student_report()

    output = capsys.readouterr().out

    assert "not found" in output

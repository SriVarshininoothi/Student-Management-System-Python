from models import Student


def test_student_creation():

    student = Student(101, "Rahul", 21, "Python", "rahul@gmail.com")

    assert student.get_student_id() == 101
    assert student.get_name() == "Rahul"
    assert student.get_age() == 21
    assert student.get_course() == "Python"
    assert student.get_email() == "rahul@gmail.com"


def test_set_name():

    student = Student(101, "Rahul", 21, "Python", "rahul@gmail.com")

    result = student.set_name("Arjun")

    assert result is True
    assert student.get_name() == "Arjun"


def test_set_invalid_name():

    student = Student(101, "Rahul", 21, "Python", "rahul@gmail.com")

    result = student.set_name("")

    assert result is False
    assert student.get_name() == "Rahul"

def test_set_age():

    student = Student(101, "Rahul", 21, "Python", "rahul@gmail.com")

    result = student.set_age(22)

    assert result is True
    assert student.get_age() == 22


def test_set_invalid_age():

    student = Student(101, "Rahul", 21, "Python", "rahul@gmail.com")

    result = student.set_age(-5)

    assert result is False
    assert student.get_age() == 21

def test_set_course():

    student = Student(101, "Rahul", 21, "Python", "rahul@gmail.com")

    result = student.set_course("Java")

    assert result is True
    assert student.get_course() == "Java"


def test_set_invalid_course():

    student = Student(101, "Rahul", 21, "Python", "rahul@gmail.com")

    result = student.set_course("")

    assert result is False
    assert student.get_course() == "Python"

def test_set_email():

    student = Student(101, "Rahul", 21, "Python", "rahul@gmail.com")

    result = student.set_email("arjun@gmail.com")

    assert result is True
    assert student.get_email() == "arjun@gmail.com"


def test_set_invalid_email():

    student = Student(101, "Rahul", 21, "Python", "rahul@gmail.com")

    result = student.set_email("invalidemail")

    assert result is False
    assert student.get_email() == "rahul@gmail.com"

def test_set_marks():

    student = Student(101, "Rahul", 21, "Python", "rahul@gmail.com")

    result = student.set_marks("Python", 90)

    assert result is True
    assert student.get_marks()["Python"] == 90


def test_set_invalid_marks():

    student = Student(101, "Rahul", 21, "Python", "rahul@gmail.com")

    result = student.set_marks("Python", 110)

    assert result is False
    assert student.get_marks() == {}

def test_set_attendance():

    student = Student(101, "Rahul", 21, "Python", "rahul@gmail.com")

    result = student.set_attendance("2026-11-18", "Present")

    assert result is True
    assert student.get_attendance()["2026-11-18"] == "Present"


def test_duplicate_attendance():

    student = Student(101, "Rahul", 21, "Python", "rahul@gmail.com")

    student.set_attendance("2026-11-18", "Present")

    result = student.set_attendance("2026-11-18", "Absent")

    assert result is False
    assert student.get_attendance()["2026-11-18"] == "Present"
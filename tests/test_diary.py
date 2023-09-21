import pytest
from lib.diary import Diary

def test_contents_not_string():
    with pytest.raises(TypeError) as e:
        Diary(123)
    assert str(e.value) == "contents must be a string"

def test_contents_empty():
    with pytest.raises(ValueError) as e:
        Diary("")
    assert str(e.value) == "contents must not be empty"

def test_contents_space():
    with pytest.raises(ValueError) as e:
        Diary(" ")
    assert str(e.value) == "contents must not be empty"

def test_contents_valid():
    diary = Diary("Hello")
    assert diary.contents == "Hello"

def test_read():
    diary = Diary("Hello")
    assert diary.read() == "Hello"

def test_read_2():
    diary = Diary("Hello\nWorld")
    assert diary.read() == "Hello\nWorld"
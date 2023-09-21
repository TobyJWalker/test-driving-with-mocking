import pytest
from lib.secret_diary import SecretDiary
from lib.diary import Diary


def test_not_diary_input():
    with pytest.raises(TypeError) as e:
        SecretDiary(123)
    assert str(e.value) == "diary must be a Diary object"

def test_diary_integration():
    diary = Diary("Hello")
    s_diary = SecretDiary(diary)
    s_diary.unlock()
    assert s_diary.read() == "Hello"
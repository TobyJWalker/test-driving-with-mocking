import pytest
from lib.secret_diary import SecretDiary
from unittest.mock import Mock
from lib.diary import Diary

def test_initialise_diary():
    diary = Diary("Hello")
    s_diary = SecretDiary(diary)
    assert s_diary.diary == diary
    assert s_diary.locked == True


def test_unlock():
    diary = Diary("Hello")
    s_diary = SecretDiary(diary)
    s_diary.unlock()
    assert s_diary.locked == False

def test_lock():
    diary = Diary("Hello")
    s_diary = SecretDiary(diary)
    s_diary.unlock()
    s_diary.lock()
    assert s_diary.locked == True

def test_read_locked():
    diary = Diary("Hello")
    s_diary = SecretDiary(diary)
    response = s_diary.read()
    assert response == "Go away!"

def test_read_unlocked():
    diary = Diary("Hello")
    diary.read = Mock(return_value="Hello")
    
    s_diary = SecretDiary(diary)
    s_diary.unlock()
    response = s_diary.read()
    assert response == "Hello"

from lib.task_list import TaskList
from unittest.mock import Mock


def test_task_list_initially_empty():
    task_list = TaskList()
    assert task_list.tasks == []


def test_tasks_initially_not_all_complete():
    task_list = TaskList()
    assert task_list.all_complete() == False

def test_adds_tasks_to_list():
    task_list = TaskList()

    # Create two mock tasks
    task_1 = Mock()
    task_2 = Mock()

    # Add the mocks to the task list
    task_list.add(task_1)
    task_list.add(task_2)

    # Assert that the task list's tasks are the mocks
    assert task_list.tasks == [task_1, task_2]

def test_tasks_all_complete():
    task_list = TaskList()

    # Create three mock tasks
    task_1 = Mock()
    task_2 = Mock()
    task_3 = Mock()

    # Set the return value of `is_complete` to True for all mocks
    task_1.is_complete.return_value = True
    task_2.is_complete.return_value = True
    task_3.is_complete.return_value = True

    # Add the mocks to the task list
    task_list.add(task_1)
    task_list.add(task_2)
    task_list.add(task_3)

    # Assert that all_complete returns True
    assert task_list.all_complete() == True

# Unit test `#tasks` and `#all_complete` behaviour
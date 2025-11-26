import pytest
from app import add_task, list_tasks, delete_task, tasks

def setup_function():
    """Clear tasks before each test."""
    tasks.clear()

def test_add_task():
    add_task("Buy groceries")
    assert len(tasks) == 1
    assert tasks[0] == "Buy groceries"

def test_add_empty_task():
    add_task("")
    assert len(tasks) == 0

def test_delete_task():
    add_task("Task 1")
    add_task("Task 2")
    delete_task("1")
    assert len(tasks) == 1
    assert tasks[0] == "Task 2"

def test_delete_invalid_index():
    add_task("Task 1")
    delete_task("5")
    assert len(tasks) == 1

def test_list_tasks():
    add_task("Task 1")
    add_task("Task 2")
    assert len(tasks) == 2

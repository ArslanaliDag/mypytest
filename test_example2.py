import os
import pytest


def read_data_from_file(file_path):
    with open(file_path, 'r') as file:
        return file.read()
    
    
@pytest.fixture
def temp_file(tmp_path):
    file_path = tmp_path / 'testfile.txt'
    with open(file_path, 'w') as f:
        f.write('Hello, World!')
    yield file_path
    # Очистка после теста
    os.remove(file_path)

@pytest.fixture
def empty_file(tmp_path):
    file_path = tmp_path / 'emptyfile.txt'
    open(file_path, 'w').close()  # Создаём пустой файл
    yield file_path
    # Очистка после теста
    os.remove(file_path)

def test_read_data_from_file(temp_file):
    data = read_data_from_file(temp_file)
    assert data == 'Hello, World!'

def test_read_data_from_empty_file(empty_file):
    data = read_data_from_file(empty_file)
    assert data == ''
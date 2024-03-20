import pytest
import os
from app.io.input import read_file_using_builtin, read_file_using_pandas


@pytest.fixture
def test_valid_text():
    content = "Hello world"
    path = "test1.txt"
    with open(path, "w") as file:
        file.write(content)
    yield path
    os.remove(path)


def test_unknown_path():
    path = "unknownfile.txt"

    with pytest.raises(FileNotFoundError):
        read_file_using_builtin(path)


def test_unknown_path_for_pandas():
    path = "anotherunknownfile.txt"

    with pytest.raises(FileNotFoundError):
        read_file_using_pandas(path)


def test_empty_path():
    path = ""

    with pytest.raises(FileNotFoundError):
        read_file_using_builtin(path)


def test_if_text_valid(test_valid_text):
    path = test_valid_text
    content = "Hello world"

    text_to_check = read_file_using_builtin(path)
    assert text_to_check == content


def test_non_supported_format():
    non_supported_file = "data/test.pdf"

    try:
        read_file_using_builtin(non_supported_file)
    except FileNotFoundError:
        raise ValueError("File format not supported")
import os
from src.file_reader import FileReader

def test_read_file():
    file_path="data/courses.txt"
    reader=FileReader()

    lines=reader.read_lines(file_path)
    assert len(lines)>0
    assert "MATH166" in lines[0]
    assert isinstance(lines, list)
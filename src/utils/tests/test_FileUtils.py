from src.utils.FilesUtils import create_tmpfile
from src.utils.FilesUtils import save_to_tmpfile


def test_temp_file_creation():
    file = create_tmpfile('test_temp_file_creation.txt')
    with open(file.name, 'w'):
        file.write(b'succeeded')
        file.seek(0)
        assert file.readlines()[0] == b'succeeded'


def test_temp_file_writing():
    file = create_tmpfile('test_temp_file_writing.txt')
    save_to_tmpfile(file, 'succeeded')
    with open(file.name):

        assert file.readlines()[0] == b'succeeded'

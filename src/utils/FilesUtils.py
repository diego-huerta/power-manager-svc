import tempfile
import itertools


def create_tmpfile(file_name: str):
    tempfile._get_candidate_names = lambda: itertools.repeat(file_name)
    return tempfile.NamedTemporaryFile(prefix='')


def save_to_tmpfile(tmpfile: tempfile.NamedTemporaryFile, rms: str):
    with open(tmpfile.name, 'w') as f:
        f.write(rms)
        f.seek(0)

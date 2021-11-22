import tempfile
import itertools


def create_tmpfile(file_name: str):
    tempfile._get_candidate_names = lambda: itertools.repeat(file_name)
    return tempfile.NamedTemporaryFile(prefix='')


def save_to_tmpfile(tmpfile: tempfile.NamedTemporaryFile, payload: list):
    with open(tmpfile.name, 'w') as f:
        out = ''
        print(payload)
        for element in payload:
            out = out + f'{element}\n'
        f.write(out)
        f.seek(0)

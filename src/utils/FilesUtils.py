import tempfile
import itertools


def create_tmpfile(file_name: str):
    tempfile._get_candidate_names = lambda: itertools.repeat(file_name)
    return tempfile.NamedTemporaryFile(prefix='')


def save_to_tmpfile(tmpfile: tempfile.NamedTemporaryFile, payload: list or float or str):
    with open(tmpfile.name, 'w') as f:
        if type(payload) == list:
            out = ''
            for element in payload:
                out = out + f'{element}\n'
            f.write(out)
        elif type(payload) == float or type(payload) == str:
            f.write(str(payload))
        else:
            raise TypeError('The format of the payload is not supported. Provide only a list, a float or a string')
        f.seek(0)

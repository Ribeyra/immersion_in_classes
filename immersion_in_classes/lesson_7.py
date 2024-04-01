import os


class FileError(Exception):
    pass


class NotReadableError(FileError):
    pass


class NotExistsError(FileError):
    pass


class File:
    def __init__(self, path):
        self.path = path

    def read(self):
        if not os.path.exists(self.path):  # alt. os.access(file_path, os.F_OK)
            raise NotExistsError
        elif not os.access(self.path, os.R_OK):
            raise NotReadableError
        else:
            return 'some data'


def read_files(path_list):
    res = []
    for path in path_list:
        file = File(path)
        try:
            data = file.read()
        except (NotExistsError, NotReadableError):
            data = None
        res.append(data)
    return res

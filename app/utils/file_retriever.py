import os
from pathlib import Path
from os import path, listdir


class FileDataRetriever:
    @staticmethod
    def retrieve():
        file = ''
        path_root = Path(os.getcwd())
        while not path.isdir(path.join(path_root, 'data')):
            path_root = path_root.parent

        for f in listdir(path.join(path_root, 'data')):
            if f.endswith('.csv'):
                file = f
                break

        file = path.join(path_root, 'data', file)

        if len(file) == 0:
            raise SystemExit('You must insert a csv file in data folder')
        elif os.stat(file).st_size == 0:
            raise SystemExit('DATASET_PATH is set to an empty file')

        return file
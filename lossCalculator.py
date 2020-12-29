import os.path

from os import path

class SourceFolderNotFound(Exception):
    def __init__(self):
        self.message = "Source folder does not exist"
        super().__init__(self.message)

DEFAULT_CLUSTER_SIZES = [512, 1024, 2048, 4096, 8192, 16384, 32768, 65536, 131072, 262144, 524288, 1048576]

class LossCalculator:

    def __init__(self, source_folder):
        if not path.exists(source_folder):
            raise SourceFolderNotFound()
        self.source_folder = source_folder
        self.number_of_files = 0
        self.total_files_space = 0
        self.wasted_space = [0] * len(DEFAULT_CLUSTER_SIZES)
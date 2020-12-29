import os

import specialPrinter

DEFAULT_CLUSTER_SIZES = [512, 1024, 2048, 4096, 8192, 16384, 32768, 65536, 131072, 262144, 524288, 1048576]

class SourceFolderNotFound(Exception):
    def __init__(self):
        self.message = "Source folder does not exist"
        super().__init__(self.message)

class LossCalculator:

    def __init__(self, source_folder):
        if not os.path.exists(source_folder):
            raise SourceFolderNotFound()
        self.source_folder = source_folder
        self.number_of_files = 0
        self.total_files_space = 0
        self.wasted_space = [0] * len(DEFAULT_CLUSTER_SIZES)

    def __process_file(self, file_path):
        file_size = os.path.getsize(file_path)
        self.number_of_files += 1
        self.total_files_space += file_size
        for x in range(len(DEFAULT_CLUSTER_SIZES)):
            if file_size < DEFAULT_CLUSTER_SIZES[x]:
                wasted_space = DEFAULT_CLUSTER_SIZES[x] - file_size
                self.wasted_space[x] += wasted_space
            else:
                wasted_space = file_size % DEFAULT_CLUSTER_SIZES[x]
                self.wasted_space[x] += wasted_space

    def __print_size_multiple_dimensions(self, size_in_bytes):
        size_in_kb = round(size_in_bytes / 1024, 2)
        size_in_mb = round(size_in_kb / 1024, 2)
        size_in_gb = round(size_in_mb / 1024, 2)
        print (str(size_in_gb) + " GB - " + str(size_in_mb) + " MB - " + str(size_in_kb) + " KB - " + str(size_in_bytes) + " B")

    def deep_loop(self):
        for root, dirs, files in os.walk(self.source_folder):
            for name in files:
                self.__process_file(os.path.join(root, name))

    def print_stats(self):
        specialPrinter.print_title("WASTED SPACE STATS")
        print()
        print("Files scanned: " + str(self.number_of_files))
        print("Total size of all files: ")
        self.__print_size_multiple_dimensions(self.total_files_space)
        print()
        specialPrinter.print_title("WASTED SPACE FOR CLUSTER SIZES")
        print()
        for x in range(len(DEFAULT_CLUSTER_SIZES)):

            cluster_size = DEFAULT_CLUSTER_SIZES[x]
            wasted_space = self.wasted_space[x]

            if cluster_size < 1000:
                print("CLUSTER size: " + str(cluster_size) + " bytes")
            else:
                print("CLUSTER size: " + str(cluster_size / 1024) + " KB")

            print("Total wasted space")
            self.__print_size_multiple_dimensions(wasted_space)
            print()
            
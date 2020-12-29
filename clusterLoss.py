import sys

from lossCalculator import LossCalculator, SourceFolderNotFound

source_folder = ""

# Check if source folder was passed as argument or not
if len(sys.argv) < 2:
    source_folder = raw_input("Enter source folder: ")
else:
    source_folder = sys.argv[1]

try:
    loss_calculator = LossCalculator(source_folder)
except SourceFolderNotFound as error:
    print(error)
import sys

from lossCalculator import LossCalculator, SourceFolderNotFound

source_folder = ""

# Check if source folder was passed as argument or not
if len(sys.argv) < 2:
    source_folder = input("Enter source folder: ")
else:
    source_folder = sys.argv[1]

try:
    loss_calculator = LossCalculator(source_folder)
    loss_calculator.deep_loop()
    loss_calculator.print_stats()
except SourceFolderNotFound as error:
    print(error)
import csv

from src.auxiliary.constant_definitions import TIMESTAMP_TICKS_FOR_GRAPHS_FOLDER


def import_timestamp_ticks(name_file, folder_name = TIMESTAMP_TICKS_FOR_GRAPHS_FOLDER):
    full_path_file = folder_name / name_file

    if not full_path_file.is_file():
        return None

    with open(folder_name / name_file, 'r', newline='') as myfile:
        wr = csv.reader(myfile, quoting=csv.QUOTE_ALL)
        wr.readrow()

        wr=wr

def import_check(name_file, folder_name):
    return (folder_name / name_file).is_file()

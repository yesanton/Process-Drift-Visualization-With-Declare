import csv

from src.auxiliary.constant_definitions import TIMESTAMP_TICKS_FOR_GRAPHS_FOLDER


def export_timestamp_ticks(timestamps, name_file, folder_name = TIMESTAMP_TICKS_FOR_GRAPHS_FOLDER):
    with open(folder_name / name_file, 'w', newline='') as myfile:
        wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
        wr.writerow(timestamps)
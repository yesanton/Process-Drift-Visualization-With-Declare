import csv
import os

from src.auxiliary.constant_definitions import FOLDER_TIMESTAMP_TICKS_FOR_GRAPHS


def export_one_line_csvs(timestamps, name_file, folder_name = FOLDER_TIMESTAMP_TICKS_FOR_GRAPHS):

    if not os.path.exists(FOLDER_TIMESTAMP_TICKS_FOR_GRAPHS):
        os.makedirs(FOLDER_TIMESTAMP_TICKS_FOR_GRAPHS)

    with open(folder_name / name_file, 'w', newline='') as myfile:
        wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
        wr.writerow(timestamps)




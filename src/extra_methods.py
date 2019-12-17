''' Methods put aside from the core technique functions

Author: Anton Yeshchenko
'''
import csv
import math
from pathlib import Path
import os
import json
import subprocess



'''# Method produces the timestamps for the graphs
'''
def timestamp_ticks(sliding_window_step, window_size, dataset_folder, dataset_name, case_ind, timestamp_ind):
    dataset_link = Path("./data_initial/"+dataset_folder + dataset_name+"_timestamp_sorted.csv")

    csvfile = open(dataset_link, 'r')
    csv_reader = csv.reader(csvfile, delimiter=',', quotechar='|')
    hh = next(csv_reader, None)

    # FOR ITALIAN HELP DESK
    # 0 - case name
    # 3 - timestamp
    # case_ind = 0
    # timestamp_ind = 3
    #
    # #for sepsis
    # case_ind = 23
    # timestamp_ind =30
    # # for traffic fines
    # case_ind = 4
    # timestamp_ind = 11
    #
    # # for bpic 2013
    # case_ind = 0
    # timestamp_ind = 3

    line = next(csv_reader, None)
    case = line[case_ind]
    timestamps = [line[timestamp_ind]]

    while line:
        if not case == line[case_ind]:
            timestamps.append(line[timestamp_ind])
            case = line[case_ind]
        line = next(csv_reader, None)

    #csvfile = open(Path('./timestamps.csv'), 'w')
    #results_writer = csv.writer(csvfile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)

    time_out = []
    n_th = 0
    number_of_timestamps = (len(timestamps) - window_size) / sliding_window_step
    skip_every_n_th = math.ceil(number_of_timestamps / 30)

    #timestamps = sorted(timestamps)
    for i in range(0,len(timestamps) - window_size, sliding_window_step):
        #print (timestamps[i] + " for from: " + str(i) + ' to ' + str(i+window_size))
        #results_writer.writerow([timestamps[i]])
        if n_th % skip_every_n_th == 0:
            time_out.append(timestamps[i][0:10])
        else:
            time_out.append(" ")
        n_th += 1
    return time_out

'''output the declare specifications in json format
per each discovered cluster (behaviour change patch)
'''

# ./run-MINERfulSimplifier.sh -iMF path_to_save  -iME json -oCSV new_file_path -prune hierarchyconflictredundancy
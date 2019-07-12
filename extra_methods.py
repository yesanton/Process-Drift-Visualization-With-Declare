''' Methods put aside from the core technique functions


Author: Anton Yeshchenko
'''
import csv
import math
from pathlib import Path
import os
import json
import subprocess

def importData(DATASET_NAME, c = True):
    if c == True:
        csvfile = open(DATASET_NAME, 'r')
    else:
        csvfile = open(DATASET_NAME, 'r')
    csv_reader = csv.reader(csvfile, delimiter=';', quotechar='|')

    hea = next(csv_reader, None)
    hea2 = next(csv_reader, None)

    hea2 = hea2[2:]
    hea = hea[2:]

    header_output = list()

    for i in range(len(hea)):
        if i % 3 == 0:
            tem_h = [hea2[i][1:-1]]
            temp = hea[i]
            if temp[0] == '\'':
                temp = temp[1:]
            if temp[-1] == '\'':
                temp = temp[:-1]
            if temp[-1] == ')':
                temp = temp[:-1]
            # now we split the string
            name_of_constraint_end_index = temp.find('(')
            tem_h.append(temp[:name_of_constraint_end_index])

            temp = temp[name_of_constraint_end_index+1:]
            #find if we have two events or one
            separated_constraints_index = temp.find(', ')
            if not separated_constraints_index == -1:
                tem_h.append(temp[:separated_constraints_index])
                tem_h.append(temp[separated_constraints_index+1:])
            else:
                tem_h.append(temp)
                tem_h.append('')
        else:
            tem_h = [hea2[i][1:-1]] + tem_h[1:]

        header_output.append(tem_h)

    sequences = list()

    # -2 is for the first two columns
    for i in range(len(hea)):
        sequences.append(list())

    corresponding_number_of_traces = []

    n_lines =0
    for r in csv_reader:
        corresponding_number_of_traces.append(r[:2])
        n_lines += 1

        counter = 0
        for i in range(len(r)):
            if counter > 1:
                sequences[i-2].append(float(r[i]))
            else:
                counter += 1

    return sequences, header_output,corresponding_number_of_traces

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
def saveConstrainsPerCluster(constraints, save_name, logFolder):
    dict_out = {}
    dict_out["constraints"] = []

    for constraint in constraints:
        temp_dict = {}
        temp_dict["template"] = constraint[0]
        temp_dict['parameters'] = []
        for par in constraint[1:]:
            if par != '':
                temp_dict['parameters'].append([par])

        dict_out["constraints"].append(temp_dict)

    new_path = 'graphs_produced_detailed' + '/' + 'constraints' + '/' + logFolder

    if not os.path.exists(new_path):
        os.makedirs(new_path)

    for key in range(len(dict_out['constraints'])):
        dict_out['constraints'][key]['template'] = dict_out['constraints'][key]['template'].rstrip().lstrip()

        #TODO put real numbers for confidence support etc.

        dict_out['constraints'][key]['support'] = 1
        dict_out['constraints'][key]['confidence'] = 1
        dict_out['constraints'][key]['interestFactor'] = 1


        for el in dict_out['constraints'][key]['parameters']:
            el[0] = el[0]


    path_to_save = new_path + '/' + save_name
    with open(path_to_save, 'w') as fp:
        json.dump(dict_out, fp)
        fp.close()


    new_file_path = 'graphs_produced_detailed' + '/' + 'constraints_pruned' + '/' + logFolder
    if not os.path.exists(new_file_path):
        os.makedirs(new_file_path)


    new_file_path = "../" + new_file_path +  '/' + save_name[:-4] + 'csv'
    # this works from the minerful folder
    # ./run-MINERfulSimplifier.sh -iMF
    #                       ../graphs_produced_detailed/constraints/italian_help_desk/italian_help_deskplot_confidence_0_100_50_ward_euclidean_300_distancecl-0.json

    #                       -iME json -oCSV 1.csv  -prune hierarchyconflictredundancy
    subprocess.run(["./run-MINERfulSimplifier.sh",
                    "-iMF",
                    '../' + path_to_save,
                    "-iME", 'json',
                    "-oCSV", new_file_path,
                    "-prune", "hierarchyconflictredundancy"],
                    cwd="minerful_scripts")

    dict_out = None

# ./run-MINERfulSimplifier.sh -iMF path_to_save  -iME json -oCSV new_file_path -prune hierarchyconflictredundancy
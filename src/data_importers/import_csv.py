import csv

from src.auxiliary.constant_definitions import FOLDER_TIMESTAMP_TICKS_FOR_GRAPHS


def import_timestamp_ticks(name_file, folder_name = FOLDER_TIMESTAMP_TICKS_FOR_GRAPHS):
    full_path_file = folder_name / name_file

    if not full_path_file.is_file():
        return None

    with open(folder_name / name_file, 'r') as myfile:
        reader = csv.reader(myfile)
        your_list = list(reader)
        return your_list[0]

def import_check(name_file, folder_name):
    return (folder_name / name_file).is_file()


def import_minerful_constraints_data(name_file, folder_name, constraint_type = "confidence"):
    csvfile = open(folder_name / name_file, 'r')
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

    # For now we only concentrate on confidence as it is most representative measure
    if constraint_type == "confidence":
        confidence = []
        for i, j in zip(sequences, header_output):
            if j[0] == "Confidence":
                confidence.append(j[1:] + i)

        return confidence
    #return sequences, header_output, corresponding_number_of_traces
    return None
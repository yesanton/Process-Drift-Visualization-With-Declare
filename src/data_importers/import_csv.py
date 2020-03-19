import csv

def import_timestamp_ticks(fileMngm):
    full_path_file = fileMngm.get_path_timestamp_ticks()

    if not full_path_file.is_file():
        return None

    with open(fileMngm.get_path_timestamp_ticks(), 'r') as myfile:
        reader = csv.reader(myfile)
        your_list = list(reader)
        return your_list[0]

def import_check(file):
    return file.is_file()

''' the output is:
constraints 
'''
def import_minerful_constraints_timeseries_data(fileMngm, algoPrmts):
    csvfile = open(fileMngm.get_path_minerful_constraints(), 'r')
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
    if algoPrmts.constraint_type_used not in set(['confidence', 'support', 'interestFactor']):
        raise ValueError(algoPrmts.constraint_type_used + " is not a constraint type")
    elif algoPrmts.constraint_type_used == 'confidence': cn = "Confidence"
    elif algoPrmts.constraint_type_used == 'support': cn = "Support"
    else: cn = "InterestF"

    constraints = []
    for i, j in zip(sequences, header_output):
        if j[0] == "Confidence":
            constraints.append(j[1:] + i)

    return constraints

def import_constraints_to_dictionary(file_name):
    store_constraints = dict()
    with open(file_name) as one_cluster_example:
        reader = csv.reader(one_cluster_example, delimiter=';', quotechar='|', quoting=csv.QUOTE_MINIMAL)
        next(reader, None)
        for row in reader:
            constr = [i[1:-1].strip() for i in row[1:4]]

            if not constr[0] in store_constraints:
                store_constraints[constr[0]] = set()
            store_constraints[constr[0]].add((constr[1], constr[2]))

    return store_constraints
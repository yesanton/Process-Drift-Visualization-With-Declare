import json

def export_constraints_per_cluster(constraints, fileMngm, file_ind):
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

    for key in range(len(dict_out['constraints'])):
        dict_out['constraints'][key]['template'] = dict_out['constraints'][key]['template'].rstrip().lstrip()

        # T$ODO put real numbers for confidence support etc.
        dict_out['constraints'][key]['support'] = 1
        dict_out['constraints'][key]['confidence'] = 1
        dict_out['constraints'][key]['interestFactor'] = 1


        for el in dict_out['constraints'][key]['parameters']:
            el[0] = el[0]

    with open(fileMngm.get_path_drift_plot_all_timeseries(file_ind), 'w') as fp:
        json.dump(dict_out, fp)
        fp.close()
    dict_out = None #  clean up
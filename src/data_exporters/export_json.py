import os
import json
import subprocess

def export_constraints_per_cluster(constraints, save_name, logFolder):
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

    if not os.path.exists(logFolder):
        os.makedirs(logFolder)

    for key in range(len(dict_out['constraints'])):
        dict_out['constraints'][key]['template'] = dict_out['constraints'][key]['template'].rstrip().lstrip()

        #TODO put real numbers for confidence support etc.

        dict_out['constraints'][key]['support'] = 1
        dict_out['constraints'][key]['confidence'] = 1
        dict_out['constraints'][key]['interestFactor'] = 1


        for el in dict_out['constraints'][key]['parameters']:
            el[0] = el[0]


    path_to_save = logFolder / save_name
    with open(path_to_save, 'w') as fp:
        json.dump(dict_out, fp)
        fp.close()


    new_file_path = logFolder /  'constraints_pruned'
    if not os.path.exists(new_file_path):
        os.makedirs(new_file_path)


    new_file_path = new_file_path / (save_name[:-4]+'csv')

    # Make a copy of the environment
    env = dict(os.environ)
    env['JAVA_OPTS'] = 'foo'

    # TODO put this inside of minerful adapter
    subprocess.call(['java', "-Xmx16G", "--add-modules", "java.xml.bind", '-cp', 'MINERful.jar', 'minerful.MinerFulSimplificationStarter',
         "-iMF",
                    str(path_to_save),
                    "-iME", 'json',
                    "-oCSV", str(new_file_path),
                    "-prune", "hierarchyconflictredundancy"], env=env,
                       cwd="minerful_scripts")
    # subprocess.run(["./run-MINERfulSimplifier.sh",
    #                 "-iMF",
    #                 '../' + path_to_save,
    #                 "-iME", 'json',
    #                 "-oCSV", new_file_path,
    #                 "-prune", "hierarchyconflictredundancy"],
    #                 cwd="minerful_scripts")

    dict_out = None

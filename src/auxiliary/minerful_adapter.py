import subprocess
import os

def mine_minerful_for_declare_constraints(fileMngm,algoPrmts):
    env = dict(os.environ)
    env['JAVA_OPTS'] = 'foo'
    subprocess.call(['java', '-version'])
    file_input = str(fileMngm.get_path_input_sorted_xes())
    file_output = str(fileMngm.get_path_minerful_constraints())

    subprocess.call(['java', "-Xmx16G", "--add-modules", "java.xml.bind", '-cp', 'MINERful.jar', 'minerful.MinerFulMinerSlider',
                     "-iLF",
                    file_input,
                    "-iLStartAt", "0", # 0 here is at which timestamp we start, we always start from the first
                     "-iLSubLen", str(algoPrmts.window_size),
                     "-sliBy", str(algoPrmts.sliding_window_size),
                    '-para', '4',
                    '-s', '0.000000001',
                    '-c', '0.0',
                    '-i', '0.0',
                     '-prune', 'none', # this is the pruning or not pruning options of constraints
                    '-sliOut',
                    file_output],
                    env=env,
                    cwd="src/minerful_scripts")

def prune_constraints_minerful(fileMngm, file_ind):
    # Make a copy of the environment
    env = dict(os.environ)
    env['JAVA_OPTS'] = 'foo'
    subprocess.call(['java', "-Xmx16G", "--add-modules", "java.xml.bind", '-cp', 'MINERful.jar',
                     'minerful.MinerFulSimplificationStarter',
                     "-iMF",
                     str(fileMngm.get_path_drift_plot_all_timeseries(file_ind)),
                     "-iME", 'json',
                     "-oCSV", str(fileMngm.get_path_drift_plot_all_timeseries_pruned(file_ind)),
                     "-prune", "hierarchy"], env=env, # or "hierarchyconflictredundancy", or the
                                                      # most accurate "hierarchyconflictredundancydouble"
                    cwd="src/minerful_scripts")



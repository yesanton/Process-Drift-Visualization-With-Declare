import subprocess
import os
from pathlib import Path

from src.auxiliary.constant_definitions import CSV_FILE_EXTENSION
from src.auxiliary.simplifiers import compose_name


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
                    cwd="minerful_scripts")
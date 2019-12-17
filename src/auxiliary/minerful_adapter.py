import subprocess
import os
from pathlib import Path

from src.auxiliary.constant_definitions import CSV_FILE_EXTENSION
from src.auxiliary.simplifiers import compose_name


def mine_minerful_for_declare_constraints(name_file_input_log,
                                          folder_file_input_log,
                                          extension_file_input_log,
                                          tStart, subL, sliBy,
                                          name_file_output, folder_file_output):

    env = dict(os.environ)
    env['JAVA_OPTS'] = 'foo'
    subprocess.call(['java', '-version'])

    file_input = str(folder_file_input_log / (name_file_input_log + extension_file_input_log))

    file_output = str(folder_file_output / name_file_output)


    subprocess.call(['java', "-Xmx16G", "--add-modules", "java.xml.bind", '-cp', 'MINERful.jar', 'minerful.MinerFulMinerSlider',
                     "-iLF",
                    file_input,
                    "-iLStartAt", str(tStart),
                     "-iLSubLen", str(subL),
                     "-sliBy", str(sliBy),
                    '-para', '4',
                    '-s', '0.000000001',
                    '-c', '0.0',
                    '-i', '0.0',
                     '-prune', 'none', # this is the pruning or not pruning options of constraints
                    '-sliOut',
                    file_output],
                    env=env,
                    cwd="minerful_scripts")
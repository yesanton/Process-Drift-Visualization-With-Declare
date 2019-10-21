import os
import subprocess

# Make a copy of the environment
env = dict(os.environ)
env['JAVA_OPTS'] = 'foo'
subprocess.call(['java', "-Xmx16G", '-cp', 'MINERful.jar' ,'minerful.MinerFulMinerSlider'], env=env,cwd="minerful_scripts")

# subprocess.run(["java -Xmx16G -cp MINERful.jar minerful.MinerFulMinerSlider",
#                     "-iLF",
#                     data_path,
#                     "-iLStartAt", str(tStart), "-iLSubLen", str(subL),
#                     '-para', '4',
#                     '-s', '0.000000001',
#                     '-c', '0.0',
#                     '-i', '0.0',
#                     '-prune', 'none',
#                     '-sliOut',
#                     "../data_from_minerful/" + dataset_moto + "_" +
#                     str(tStart) + "_" + str(subL) + "_" + str(sliBy) + '.csv',
#                     "-sliBy", str(sliBy),
#                     " -shush"], cwd="minerful_scripts")
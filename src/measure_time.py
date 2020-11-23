import os
import time

from auxiliary.constant_definitions import FOLDER_DATA_RESULTS_FINAL
from auxiliary.data_structures import FilesManagement
from data_exporters.export_csv import export_many_line_csvs

# log = 'Loop'
# parameters = '-logName ' + log + ' -subL 800 -sliBy 400  -cluCut 600 -noSort'
#
# log = 'ConditionalRemoval'
# parameters = '-logName ' + log + ' -subL 1000 -sliBy 500  -cluCut 600 -noSort'

# log = 'OIR'
# parameters = '-logName OIR -subL 400  -sliBy 200  -cluCut 500 -noSort'

# log = 'ConditionalMove'
# parameters = '-logName ' + log + ' -subL 1000 -sliBy 500  -cluCut 600 -noSort'

# log = 'Sepsis'
# parameters = '-logName ' + log + ' -subL 100 -sliBy 50 -cluCut 600 -noSort'

log = 'bpic_2011_hospital'
parameters = '-logName ' + log + ' -subL 100 -sliBy 50 -cluCut 1200 -noSort'

# log = 'italian_help_desk'
# parameters = '-logName ' + log + ' -subL 200  -sliBy 100  -cluCut 300 -noSort'


times = []
times.append(['event log', log])


begin = time.time()
os.system("python3 scenario_1.py " + parameters)
end = time.time()
times.append(['steps2-4', end-begin])

os.system("python3 scenario_2.py " + parameters)
end2 = time.time()
times.append(['step1+6', end2-end])


os.system("python3 scenario_3.py " + parameters)
os.system("python3 scenario_4_ex.py " + parameters)
os.system("python3 scenario_5_ex.py " + parameters)
end3 = time.time()
times.append(['step5', end3-end2])

times.append(['total', end3 - begin])

# total time taken
print(f"Total runtime of the program is {end3 - begin}")

export_many_line_csvs(times, FOLDER_DATA_RESULTS_FINAL / ('time_measurement_' + log + '.csv'))
'''
script to find the average change in the constraint measure,
to find how the stable-drifting the event log is

author: Anton Yeshchenko

examples to run:
-logName bpi_challenge_2013_incidents -subL 400 -sliBy 150
-logName Sepsis -subL 50 -sliBy 25
-logName ConditionalRemoval -subL 1000 -sliBy 500
-logName Loop -subL 800 -sliBy 400
-logName italian_help_desk -subL 200 -sliBy 75
-logName OIR -subL 400  -sliBy 200
-logName bpic_2011_hospital -subL 40 -sliBy 20

'''
from auxiliary.command_line import get_commandline_parameters
from data_algorithms_cluster_and_change_point import remove_redundant_timeseries_HEADER
from data_importers.import_csv import import_minerful_constraints_timeseries_data
from statistics import mean

fileMngm, algoPrmts = get_commandline_parameters()

constraints = import_minerful_constraints_timeseries_data(fileMngm, algoPrmts)
constraints = remove_redundant_timeseries_HEADER(constraints)


measure = mean([max(co[3:]) - min(co[3:]) for co in constraints])

print("average spread of all measures: " + str(measure))





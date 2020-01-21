'''
Augmented Dickey-Fuller test
'''
import csv
import numpy as np
from src.auxiliary.command_line import get_commandline_parameters
from pandas import read_csv
from statsmodels.tsa.stattools import adfuller
# https://machinelearningmastery.com/time-series-data-stationary-python/
from src.data_importers.import_csv import import_check

fileMngm, algoPrmts = get_commandline_parameters()


#
# patthh = fileMngm.get_path_drift_plot_averaged_timeseries(10)
# # patthh = 'C:\Users\anton\Documents\WritePrograms\Process-Drift-Visualization-With-Declare\data\data_results_final\traffic_fines_1\graphs\drift_plots\timeseries\10traffic_fines_1_1000_500_ward_euclidean_1000_distance.csv'
# #\
curr_ind = 0
while import_check(fileMngm.get_path_drift_plot_averaged_timeseries(curr_ind)):
    b = []

    with open(fileMngm.get_path_drift_plot_averaged_timeseries(curr_ind)) as save_time_series_per_cl:
        r = csv.reader(save_time_series_per_cl, dialect='excel')
        for a in r:
            for i in a:
                b.append(float(i))
    X = np.array(b)

    result = adfuller(X)

    print("Data number " + str(curr_ind))
    print('ADF Statistic: %f' % result[0])
    print('p-value: %f' % result[1])
    print('Critical Values:')
    for key, value in result[4].items():
        print('\t%s: %.3f' % (key, value))

    curr_ind += 1
# Running the example prints the test statistic value of -4. The more negative this statistic,
# more likely we are to reject the null hypothesis (we have a stationary dataset).
#
# As part of the output, we get a look-up table to help determine the ADF statistic. We can see that
# our statistic value of -4 is less than the value of -3.449 at 1%.
#
# This suggests that we can reject the null hypothesis with a significance level of less than 1%
# (i.e. a low probability that the result is a statistical fluke).
#
# Rejecting the null hypothesis means that the process has no unit root, and in turn that the time
# series is stationary or does not have time-dependent structure.
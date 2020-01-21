import csv
import numpy as np
import matplotlib.pyplot as plt
import statsmodels.api as sm
from src.data_importers.import_csv import import_check
# function from here: https://www.statsmodels.org/stable/generated/statsmodels.graphics.tsaplots.plot_acf.html
# info  https://towardsdatascience.com/almost-everything-you-need-to-know-about-time-series-860241bdc578
# https://campus.datacamp.com/courses/visualizing-time-series-data-in-python/seasonality-trend-and-noise?ex=1


new_path = 'graphs_produced_detailed' + '/' + 'timeseries' + '/'
name_file = 'italian_help_deskitalian_help_deskplot_confidence_0_200_50_ward_euclidean_300_distance_changepoints_separatelycl-'
name_file_end = '.png.csv'

def visualize_autocorrelation_plots(fileMngm, lag_for_autocorrelation = 20):
    curr_ind = 0
    while import_check(fileMngm.get_path_drift_plot_averaged_timeseries(curr_ind)):
        with open(fileMngm.get_path_drift_plot_averaged_timeseries(curr_ind)) as save_time_series_per_cl:
            r = csv.reader(save_time_series_per_cl, dialect='excel')
            b = []
            for a in r:
                b.append(a)
        if len(b[0]) < 20:
            lag_for_autocorrelation = 10
        sm.graphics.tsa.plot_acf(np.array(b[0]).astype(np.float), lags=lag_for_autocorrelation)
        plt.savefig(fileMngm.get_path_autocorrelation_graphs_for_constraints(curr_ind), bbox_inches='tight')
        plt.close()
        print('autocorrelation plot ' + str(curr_ind) + ' plotted')
        curr_ind += 1
import csv

import numpy as np
import matplotlib.pyplot as plt
import statsmodels.api as sm
# function from here: https://www.statsmodels.org/stable/generated/statsmodels.graphics.tsaplots.plot_acf.html
# info  https://towardsdatascience.com/almost-everything-you-need-to-know-about-time-series-860241bdc578
# https://campus.datacamp.com/courses/visualizing-time-series-data-in-python/seasonality-trend-and-noise?ex=1
new_path = 'graphs_produced_detailed' + '/' + 'timeseries' + '/'
name_file = 'italian_help_deskitalian_help_deskplot_confidence_0_200_50_ward_euclidean_300_distance_changepoints_separatelycl-'
name_file_end = '.png.csv'


for i in range(17):
    with open("../" + new_path +  name_file + str(i) + name_file_end) as save_time_series_per_cl:
        r = csv.reader(save_time_series_per_cl, dialect='excel')
        b = [ ]
        for a in r:
            b.append(a)
    lags = 20
    sm.graphics.tsa.plot_acf(np.array(b[0]).astype(np.float), lags=lags)
    plt.savefig("../" + new_path + '/' + name_file + str(lags) + '-' + str(i) + ".png", bbox_inches='tight')

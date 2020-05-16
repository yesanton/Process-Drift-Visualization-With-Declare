''' clustering and change point methods are here

Author: Anton Yeshchenko
'''
from sklearn.metrics import mean_squared_error
import numpy as np
import ruptures as rpt
from scipy.cluster.hierarchy import dendrogram, linkage
from scipy.cluster.hierarchy import fcluster
import numpy

# method used in the main processing method for cleaning data
# removes all unchanging or stable time-series
def remove_redundant_timeseries_HEADER(data_uncut):
    data = []
    zeros_removed = 0
    hundreds_removed = 0
    nonchaning_removed = 0

    def all_list_in_interval(L):
        for i in L[1:]:
            if i < 1.05 * L[0] and i > L[0] * 0.95:
                continue
            else:
                return False
        return True

    for j in data_uncut:
        i = j[3:]
        if (mean_squared_error(i, [0] * len(i)) < 10):
            zeros_removed += 1
        elif mean_squared_error(i, [100] * len(i)) < 1:
            hundreds_removed += 1
        elif all_list_in_interval(i):
            nonchaning_removed += 1
        else:
            data.append(j)

    print('there are : ' + str(len(data)) + " values left after deleting 100, and 0s")
    print("there were: " + str(zeros_removed) + " vectors with zeros removed")
    print("there were: " + str(hundreds_removed) + " vectors with hundreds removed")
    print("there were: " + str(nonchaning_removed) + " vectors with non changing values removed")

    return data

def sort_by_closest_neigbour_HEADER(data):
    print ('there were : ' + str(len(data)) + " values")
    # we start attaching other vectors to this one
    new_data = [[100] * len(data[0])]

    index_set = set(range(len(data)))

    while not index_set == set():
        min_ind = 0
        min_dist = 1000000
        for i in index_set:
            d = mean_squared_error(data[i][3:], new_data[-1][3:])
            if d < min_dist:
                min_ind = i
                min_dist = d
        new_data.append(data[min_ind])
        print ("sorted: " + str(len(new_data)-1) + " out of: " + str(len(data)))
        index_set.remove(min_ind)

    return new_data[1:]

# main method of data analysis
# the clusters and the change points are found here
def do_cluster_changePoint(data_uncut, algoPrmts):
    # first step is to use only those constrains that are changing
    data_uncut = remove_redundant_timeseries_HEADER(data_uncut)

    # delete headers
    data_cut = []
    for data_point in data_uncut:
        data_cut.append(data_point[3:])

    '''build the clustering method'''
    Z = linkage(data_cut, method=algoPrmts.linkage_method, metric=algoPrmts.linkage_metric) # metric='correlation'
    a = fcluster(Z, algoPrmts.clustering_cutoff_param, algoPrmts.fcluster_metric)

    d = dict()
    for cluster_n, data in zip(a,data_uncut):
        if not cluster_n in d:
            d[cluster_n] = [data]
        else:
            d[cluster_n].append(data)

    data = []
    y_lines = []
    count = 0
    clusters_with_declare_names = {}

    order_cluster = [(i, len(d[i])) for i in d.keys()]
    order_cluster = sorted(order_cluster, key=lambda x : -x[1])
    order_cluster = [key for key, _ in order_cluster]

    for key in order_cluster:
        # preprocess the clusters for plotting better (sorting them by similarity)
        if not algoPrmts.no_sort_in_clusters:
            d[key] = sort_by_closest_neigbour_HEADER(d[key])

        clusters_with_declare_names[key] = [d[key][0][:3]]
        data.append(d[key][0][3:])

        for i in d[key][1:]:
            clusters_with_declare_names[key].append(i[:3])
            data.append(i[3:])
        count += len(d[key])
        y_lines.append(count)
        print ("Cluster size: " + str(len(d[key])))
    print ('number of clusters: ' + str(len(d)))

    '''NOW find the horisontal cluster
       now we use unclastured cut data(without header)
    '''
    # algorithm of how to detect the best penalty value for the
    # change point detection
    def dingOptimalNumberOfPoints(algo):
        point_detection_penalty = 50
        x_lines = algo.predict(pen=point_detection_penalty)

        while point_detection_penalty >= len(x_lines):
            point_detection_penalty -= 1
            x_lines = algo.predict(pen=point_detection_penalty)

        if len(x_lines) > 15:
            x_lines = x_lines[-1:]
        return x_lines

    x_all_lines = {}
    # in ths case we want to detect the drifts in the whole range of constrains at the same time
    c = rpt.costs.CostRbf();

    if algoPrmts.change_point_for_all:
        dd = []
        for dk in order_cluster:
            for  i in d[dk]:
                dd.append(i[3:])

        sig = np.array(dd)
        signal = np.transpose(sig)
        algo = rpt.Pelt(model="rbf", custom_cost=c).fit(signal)
        x_lines = dingOptimalNumberOfPoints(algo)
        x_all_lines[0] = x_lines
        # pen - penalizing the number of change points
    else:
        dd = []
        for dk in order_cluster:
            for i in d[dk]:
                dd.append(i[3:])

            sig = np.array(dd)
            signal = np.transpose(sig)
            algo = rpt.Pelt(model="rbf", custom_cost=c, min_size=2,jump=2).fit(signal)

            x_lines = dingOptimalNumberOfPoints(algo)
            x_all_lines[dk] = x_lines
            sig = None
            signal = None
            algo = None
            dd = []

    # print some info
    print ('x lines: ')
    print (x_lines)
    print ("clusters were ordered in the : ")
    print(order_cluster)

    return data, y_lines, x_all_lines, clusters_with_declare_names, d, order_cluster

def calculate_erratic_value(power_smooth, xnew, averaged_line):
    # some dumb way to smooth the line
    ynew = [(power_smooth[0] + power_smooth[1] + power_smooth[2]) / 3] + \
           [(power_smooth[0] + power_smooth[1] + power_smooth[2] + power_smooth[3]) / 4] + \
           [(i + j + k + l + g) / 5 for i, j, k, l, g in
            zip(power_smooth[:-4], power_smooth[1:-3], power_smooth[2:-2], power_smooth[3:-1], power_smooth[4:])] + \
           [(power_smooth[-4] + power_smooth[-3] + power_smooth[-2] + power_smooth[-1]) / 4] + \
           [(power_smooth[-3] + power_smooth[-2] + power_smooth[-1]) / 3]

    standard_erratic_as_ideal = 0
    real_erratic_score = 0 #9

    # calculate erratic measure (described in the paper)
    y_0 = ynew[0]

    y_0_polyline = power_smooth[0]
    polyline_erratic_score = 0

    for (y,y_original) in zip(ynew[1:], power_smooth[1:]):
        standard_erratic_as_ideal += xnew[1] - xnew[0]
        # multiplied by len(averaged_line)
        # to get the calculation of the line as in the squared plot (length of the curve)
        real_erratic_score += numpy.math.sqrt((xnew[1] - xnew[0]) ** 2 + ((y - y_0) * len(averaged_line)) ** 2)

        # get the erratic score as in the paper (polyline)
        # polyline_erratic_score += numpy.math.sqrt((xnew[1] - xnew[0]) ** 2 + ((y_original - y_0_polyline) * len(averaged_line)) ** 2)
        polyline_erratic_score += numpy.math.sqrt(1 + ((y_original - y_0_polyline) * len(averaged_line)) ** 2)


        y_0 = y
        y_0_polyline = y_original

    print("without DRIFT: " + str(standard_erratic_as_ideal))
    print("current DRIFT (curve length): " + str(real_erratic_score))
    print("current DRIFT (polyine length): " + str(polyline_erratic_score))

    return standard_erratic_as_ideal, polyline_erratic_score
import csv
from pathlib import Path
from sklearn.metrics import mean_squared_error
import numpy as np
import ruptures as rpt


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


def cluster_hierarcical(data_uncut, linkage_method = 'ward', linkage_metric = 'euclidean', fcluster_value = 800, fcluster_metric = 'distance', driftAll = False, noSort = False):
    # first step is to use only those constrains that are changing
    data_uncut = remove_redundant_timeseries_HEADER(data_uncut)

    from scipy.cluster.hierarchy import dendrogram, linkage
    import matplotlib.pyplot as plt
    from scipy.cluster.hierarchy import fcluster

    # delete headers
    data_cut = []
    for data_point in data_uncut:
        data_cut.append(data_point[3:])

    # 'euclidean'
#    Z = linkage(data_cut, method='weighted', metric='correlation')  # metric='correlation'
    Z = linkage(data_cut, method=linkage_method, metric=linkage_metric) # metric='correlation'

#    a = fcluster(Z, 400, 'distance')
    a = fcluster(Z, fcluster_value, fcluster_metric)
#    a = fcluster(Z, 10, 'maxclust')

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
        if not noSort:
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




    #TODO
    # Check all this
    # NOW find the horisontal cluster
    # now we use unclastured cut data(without header)

#    EXPERIMENTING WITH PARTIAL DETECTION
    def dingOptimalNumberOfPoints(algo):
        point_detection_penalty = 50
        x_lines = algo.predict(pen=point_detection_penalty)


        while point_detection_penalty >= len(x_lines):
            point_detection_penalty -= 1
            x_lines = algo.predict(pen=point_detection_penalty)
        return x_lines


    x_all_lines = {}
    # in ths case we want to detect the drits in the whole range of constrains at the same time
    if driftAll:
        dd = []
        for dk in order_cluster:
            for  i in d[dk]:
                dd.append(i[3:])

        sig = np.array(dd)
        signal = np.transpose(sig)
        algo = rpt.Pelt(model="rbf").fit(signal)

        x_lines = dingOptimalNumberOfPoints(algo)
        x_all_lines[0] = x_lines
    # TODO uncomment
    #     sig = np.array(data_cut)
    #     signal = np.transpose(sig)
    #     algo = rpt.Pelt(model="rbf").fit(signal)
        #TODO incidents
    #    x_lines = algo.predict(pen=3)
        # pen - penalizing the number of change points

    else:

        dd = []
        for dk in order_cluster:
            for i in d[dk]: #TODO change
                dd.append(i[3:])

            sig = np.array(dd)
            signal = np.transpose(sig)
            algo = rpt.Pelt(model="rbf", min_size=2,jump=2).fit(signal)

            x_lines = dingOptimalNumberOfPoints(algo)

            x_all_lines[dk] = x_lines

            sig = None
            signal = None
            algo = None
            dd = []

    print ('x lines: ')
    print (x_lines)


    print ("clusters were ordered in the : ")
    print(order_cluster)
    return data, y_lines, x_all_lines, clusters_with_declare_names, d, order_cluster


''' draw drift plots

Author: Anton Yeshchenko
'''
import matplotlib.pyplot as plt2
from scipy.interpolate import make_interp_spline, BSpline

def draw_drift_plot_for_one_cluster(ts=None,
                                    clusters_dict=None,
                                    key=None,
                                    vertical=None,
                                    file_ind = None,
                                    fileMngm=None):
    averaged_line = [0] * (len(clusters_dict[key][0]) - 3)

    for i in range(len(clusters_dict[key])):
        for j in range(len(averaged_line)):
            averaged_line[j] += clusters_dict[key][i][j + 3]

    for j in range(len(averaged_line)):
        averaged_line[j] /= len(clusters_dict[key]) * 100

    xnew = range(0, len(averaged_line))
    spl = make_interp_spline(range(len(averaged_line)), averaged_line, k=2)  # BSpline object
    power_smooth = spl(xnew)
    plt2.clf()

    plt2.stackplot(xnew, power_smooth)  # , labels=['A', 'B', 'C']
    if vertical:
        if len(vertical) > 1:
            vert = vertical[key]
        else:
            try:
                vert = vertical[list(vertical.keys())[0]]
            except KeyError:
                print ("here is the problem!")
        vert = vert[:-1]
        for line in vert:
            plt2.axvline(x=line, color='black', dashes=(2, 2))
    plt2.xticks(xnew, ts, rotation='vertical')
    plt2.ylim(top=1)

    # export the image
    plt2.savefig(fileMngm.get_path_drift_plot(file_ind), bbox_inches='tight')
    plt2.cla()
    plt2.clf()
    plt2.close()
    return power_smooth, xnew, averaged_line

# This function draws Drift plots for each cluster and returns the Erratic measure of that cluster
def drawDriftPlotforAllClusters(ts = None, clusters_dict=None, cluster_order = None):
    lines_for_lineplot = []
    for key in cluster_order:
        averaged_line = [0] * (len(clusters_dict[key][0]) - 3)
        for i in range(len(clusters_dict[key])):
            for j in range(len(averaged_line)):
                averaged_line[j] += clusters_dict[key][i][j + 3]
        lines_for_lineplot.append(averaged_line)

    # Data
    x = range(0, len(lines_for_lineplot[0]))
    plt2.clf()
    # Plot
    plt2.stackplot(x, lines_for_lineplot)
    plt2.xticks(x, ts, rotation='vertical')
    plt2.legend(loc='upper left')
    plt2.show()

    plt2.cla()
    plt2.clf()
    plt2.close()

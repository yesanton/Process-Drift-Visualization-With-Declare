''' the main script that describes drawing of the DriftMAP

Author: Anton Yeshchenko
'''
import seaborn as sns; sns.set()
import matplotlib.pylab as plt
import copy
import pandas as pd
# more details on the python lib:
# https://stackoverflow.com/questions/33282368/plotting-a-2d-heatmap-with-matplotlib

def draw_drift_map_with_clusters(data, fileMngm, algoPrmts, ts = None, y_lines = None, x_lines_all = None, cluster_order = None):
    data_c = copy.deepcopy(data)
    for i in range(len(data)):
        for j in range(len(data[i])):
            data_c[i][j] = data[i][j]/100

    #https://matplotlib.org/examples/color/colormaps_reference.html
    # copper
    # viridis
    ax = sns.heatmap(data_c, linewidth=0, cmap=algoPrmts.color_theme_drift_map, xticklabels=ts) #cmap="PiYG"

    # in case of debug to show directly here
    #plt.show()

    # draw horizontal lines
    lines = [y_lines] * (len(data_c[0])+1)
    dataT = pd.DataFrame(lines)
    asx = sns.lineplot(data=dataT,legend=False, palette=['white'] * len(y_lines), dashes = [(2, 2)] * len(y_lines), linewidth=1) #, dashes=[(2, 2), (2, 2)]

    # here is the same but faster
    if x_lines_all:
        if len(x_lines_all) == 1:
            ax.vlines(next(iter(x_lines_all.values())), *ax.get_ylim(), colors='white', linestyles='-.', linewidth=1)
        # here draw per cluster
        else:
            to_ind = 0

            for i,j in zip(cluster_order, y_lines):
                from_ind = to_ind
                to_ind =  j
                for k in x_lines_all[i]:
                    plt.plot([k,k],[from_ind, to_ind], linestyle='-.', color='white', linewidth=1)
   # ax.tight_layout()
    ax.get_figure().savefig(fileMngm.get_path_drift_map(), bbox_inches='tight')

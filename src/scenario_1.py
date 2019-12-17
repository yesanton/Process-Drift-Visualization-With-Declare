''' main script for the algorithm execution
Example run:
python3 draw_graph.py -logName bpi_challenge_2013_open  -subL 100 -sliBy 50 -driftAll
call help to see argument list

Author:  Anton Yeshchenko
'''

from src.agregated_functions import process_constraints
from src.auxiliary.constant_definitions import FOLDER_DATA_INITIAL_LOGS, FOLDER_DATA_TIMESTAMP_SORTED_LOGS, \
    XES_FILE_EXTENSION, FOLDER_DATA_MINERFUL_DECLARE_CONSTRAINTS, CSV_FILE_EXTENSION, PNG_FILE_EXTENSION, \
    FOLDER_GRAPHS_DRIFT_MAPS
from src.auxiliary.mine_features_from_data import save_separately_timestamp_for_each_constraint_window
from src.auxiliary.simplifiers import compose_name
from src.data_algorithms import do_cluster_changePoint
from src.auxiliary.command_line import get_commandline_parameters
from src.draw_drift_map import draw_drift_map_with_clusters
from src.data_exporters.export_csv import export_one_line_csvs
from src.data_exporters.export_xes import export_xes_log
from src.data_importers.import_csv import import_timestamp_ticks, import_check, import_minerful_constraints_data
from src.data_importers.import_xes import import_xes_and_sort_timestamp, import_xes
from src.auxiliary.minerful_adapter import mine_minerful_for_declare_constraints

dataset_name, \
tStart, \
subL, \
sliBy, \
fcluster_value, \
fcluster_metric, \
linkage_method, \
linkage_metric,\
driftAll, \
noSort, \
colorTheme \
    = get_commandline_parameters()

log = import_xes(FOLDER_DATA_TIMESTAMP_SORTED_LOGS, compose_name(dataset_name, XES_FILE_EXTENSION))
if not log:
    log = import_xes_and_sort_timestamp(compose_name(dataset_name,XES_FILE_EXTENSION), FOLDER_DATA_INITIAL_LOGS)
    export_xes_log(log, compose_name(dataset_name,XES_FILE_EXTENSION), FOLDER_DATA_TIMESTAMP_SORTED_LOGS)

if not import_check(compose_name(dataset_name,tStart,subL,sliBy,CSV_FILE_EXTENSION), FOLDER_DATA_MINERFUL_DECLARE_CONSTRAINTS):
    mine_minerful_for_declare_constraints(dataset_name, FOLDER_DATA_TIMESTAMP_SORTED_LOGS, XES_FILE_EXTENSION,
                                          tStart, subL, sliBy,
                                          name_file_output=compose_name(dataset_name,tStart,subL,sliBy,CSV_FILE_EXTENSION),
                                          folder_file_output=FOLDER_DATA_MINERFUL_DECLARE_CONSTRAINTS)


ts = import_timestamp_ticks(compose_name(dataset_name, sliBy, subL, CSV_FILE_EXTENSION))
if not ts:
    ts = save_separately_timestamp_for_each_constraint_window(
                 sliding_window_step=sliBy,
                 window_size=subL,
                 log= log)
    export_one_line_csvs(ts, compose_name(dataset_name, sliBy, subL, CSV_FILE_EXTENSION))


# TODO understand and change the input
confidence = import_minerful_constraints_data(
                 compose_name(dataset_name, tStart, subL, sliBy, CSV_FILE_EXTENSION),
                 FOLDER_DATA_MINERFUL_DECLARE_CONSTRAINTS)



confidence, \
cluster_bounds, \
horisontal_separation_bounds_by_cluster, \
clusters_with_declare_names, \
clusters_dict, \
cluster_order = \
    do_cluster_changePoint(confidence, linkage_method, linkage_metric, fcluster_value, fcluster_metric,
                           driftAll, noSort)

def Average(lst):
    return sum(lst) / len(lst)
for i in clusters_dict[cluster_order[4]]:
    print(i[0], i[1], i[2])
    print(min(i[3:]))
    print(max(i[3:]))
    print(Average(i[3:]))


append_name = linkage_method + '_' + linkage_metric + '_' + str(fcluster_value) + '_' + fcluster_metric
if not driftAll:
     append_name += "_changepoints_separately"
file_name_out = compose_name(dataset_name, "plot_confidence", tStart, subL, sliBy, append_name, PNG_FILE_EXTENSION)

draw_drift_map_with_clusters(confidence,
                             file_name_out,
                             FOLDER_GRAPHS_DRIFT_MAPS,
                             ts=ts,
                             y_lines=cluster_bounds,
                             x_lines_all=horisontal_separation_bounds_by_cluster,
                             cluster_order = cluster_order,
                             color_theme=colorTheme)

print('confidence graph drawn with a name: ' + file_name_out)

# drawStackedAll(ts=ts, clusters_dict=clusters_dict, cluster_order = cluster_order)

# todo handle now each cluster of constraints in the following function
process_constraints(cluster_order,
                    dataset_name,
                    tStart,
                    subL,
                    sliBy,
                    append_name,
                    clusters_with_declare_names,
                    file_name_out,
                    ts,
                    clusters_dict,
                    horisontal_separation_bounds_by_cluster,
                    erratic_measure_out = True,
                    drift_plots = True,
                    export_constraints = True,
                    export_constraints_simplified = True)





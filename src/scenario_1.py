from pathlib import Path

from src.auxiliary.constant_definitions import DATA_INITIAL_LOGS_FOLDER, DATA_TIMESTAMP_SORTED_LOGS_FOLDER, \
    XES_FILE_EXTENSION, DATA_MINERFUL_DECLARE_CONSTRAINTS_FOLDER, CSV_FILE_EXTENSION
from src.auxiliary.mine_features_from_data import save_separately_timestamp_for_each_constraint_window
from src.auxiliary.simplifiers import compose_name
from src.clustering_changePoint_methods import do_cluster_changePoint
from src.command_line import get_commandline_parameters
from src.data_exporters.export_csv import export_timestamp_ticks
from src.data_exporters.export_xes import export_xes_log
from src.data_importers.import_csv import import_timestamp_ticks, import_check
from src.data_importers.import_xes import import_xes_and_sort_timestamp, import_xes
from src.extra_methods import importData
from src.minerful_adapter import mine_minerful_for_declare_constraints

dataset_name, \
tStart, subL, sliBy, \
noMinerful, \
fcluster_value, fcluster_metric, linkage_method, linkage_metric,\
driftAll, noSort\
    = get_commandline_parameters()

log = import_xes(DATA_TIMESTAMP_SORTED_LOGS_FOLDER, compose_name(dataset_name,XES_FILE_EXTENSION))
if not log:
    log = import_xes_and_sort_timestamp(compose_name(dataset_name,XES_FILE_EXTENSION), DATA_INITIAL_LOGS_FOLDER)
    export_xes_log(log, compose_name(dataset_name,XES_FILE_EXTENSION), DATA_TIMESTAMP_SORTED_LOGS_FOLDER)

if not import_check(compose_name(dataset_name,tStart,subL,sliBy,CSV_FILE_EXTENSION), DATA_MINERFUL_DECLARE_CONSTRAINTS_FOLDER):
    mine_minerful_for_declare_constraints(dataset_name, DATA_TIMESTAMP_SORTED_LOGS_FOLDER, XES_FILE_EXTENSION,
                                      tStart, subL, sliBy,
                                      name_file_output=compose_name(dataset_name,tStart,subL,sliBy,CSV_FILE_EXTENSION),
                                      folder_file_output=DATA_MINERFUL_DECLARE_CONSTRAINTS_FOLDER)


ts = import_timestamp_ticks(compose_name(dataset_name, sliBy, subL, CSV_FILE_EXTENSION))
if not ts:
    ts = save_separately_timestamp_for_each_constraint_window(
                 sliding_window_step=sliBy,
                 window_size=subL,
                 log= log)
    export_timestamp_ticks(ts, compose_name(dataset_name, sliBy, subL, CSV_FILE_EXTENSION))


plot_with_hierarchy_clustering = True
if plot_with_hierarchy_clustering:

    # TODO change this right away
    dataset_link = Path(
        "data_from_minerful/" + dataset_name + "_" + str(tStart) + "_" + str(subL) + "_" + str(sliBy) + '.csv')
    sequences, hea, _ = importData(dataset_link)
    # For now we only concentrate on confidence as it is most representative measure
    confidence = []
    for i, j in zip(sequences, hea):
        if j[0] == "Confidence":
            confidence.append(j[1:] + i)

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



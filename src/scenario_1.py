from pathlib import Path

from src.auxiliary.constant_definitions import DATA_INITIAL_LOGS_FOLDER, DATA_TIMESTAMP_SORTED_LOGS_FOLDER, \
    XES_FILE_EXTENSION, DATA_MINERFUL_DECLARE_CONSTRAINTS_FOLDER
from src.clustering_changePoint_methods import do_cluster_changePoint
from src.command_line import get_commandline_parameters
from src.data_exporters.export_xes import export_xes_log
from src.data_importers.import_xes import import_xes_and_sort_timestamp, import_xes
from src.extra_methods import importData
from src.minerful_adapter import mine_minerful_for_declare_constraints

dataset_name, \
tStart, subL, sliBy, \
noMinerful, \
fcluster_value, fcluster_metric, linkage_method, linkage_metric,\
driftAll, noSort\
    = get_commandline_parameters()

log = import_xes(DATA_TIMESTAMP_SORTED_LOGS_FOLDER, (dataset_name + XES_FILE_EXTENSION))
if not log:
    log = import_xes_and_sort_timestamp(DATA_INITIAL_LOGS_FOLDER, (dataset_name + XES_FILE_EXTENSION))
    export_xes_log(log, DATA_TIMESTAMP_SORTED_LOGS_FOLDER, (dataset_name + XES_FILE_EXTENSION))

if not noMinerful:
    mine_minerful_for_declare_constraints(DATA_TIMESTAMP_SORTED_LOGS_FOLDER, dataset_name, XES_FILE_EXTENSION,
                                      tStart, subL, sliBy,
                                      DATA_MINERFUL_DECLARE_CONSTRAINTS_FOLDER)


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

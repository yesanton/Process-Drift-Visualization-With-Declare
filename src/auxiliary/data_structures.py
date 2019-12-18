import os
from src.auxiliary.simplifiers import compose_name
from src.auxiliary.constant_definitions import FOLDER_DATA_TIMESTAMP_SORTED_LOGS, XES_FILE_EXTENSION, \
    FOLDER_DATA_INITIAL_LOGS, CSV_FILE_EXTENSION, FOLDER_DATA_MINERFUL_DECLARE_CONSTRAINTS, \
    FOLDER_TIMESTAMP_TICKS_FOR_GRAPHS, PNG_FILE_EXTENSION, FOLDER_GRAPHS_DRIFT_MAPS, FOLDER_GRAPHS_STATISTICS, \
    FOLDER_GRAPHS_DRIFT_AVERAGED_TIMESERIES, JSON_FILE_EXTENSION, \
    FOLDER_GRAPHS_DRIFT_ALL_CONSTRAINTS_IN_CLUSTERS, FOLDER_GRAPHS_DRIFT_ALL_CONSTRAINTS_IN_CLUSTERS_PRUNED, \
    FOLDER_GRAPHS_DRIFT_PLOTS_PLOTS, FOLDER_GRAPHS_DFG


class FilesManagement:
    def __init__(self, log_name, algoPrmt):
        self.log_name = log_name
        self.namefile_minerful_constr = compose_name(log_name,
                                                 algoPrmt.window_size,
                                                 algoPrmt.sliding_window_size,
                                                 CSV_FILE_EXTENSION)
        self.namefile_timestamp_ticks = compose_name(log_name,
                                                 algoPrmt.window_size,
                                                 algoPrmt.sliding_window_size,
                                                 CSV_FILE_EXTENSION)

        self.name_file_drift_map = compose_name(log_name,
                     algoPrmt.constraint_type_used,
                     algoPrmt.window_size,
                     algoPrmt.sliding_window_size,
                     algoPrmt.linkage_method,
                     algoPrmt.linkage_metric,
                     algoPrmt.clustering_cutoff_param,
                     algoPrmt.fcluster_metric)
        if algoPrmt.change_point_for_all:
            self.name_file_drift_map = compose_name(self.name_file_drift_map,
                                                    PNG_FILE_EXTENSION)
        else:
            self.name_file_drift_map = compose_name(self.name_file_drift_map,
                                                    "changepoints_separately",
                                                    PNG_FILE_EXTENSION)

        self.name_file_erratic = compose_name(log_name,
                                              algoPrmt.window_size,
                                              algoPrmt.sliding_window_size,
                                              algoPrmt.linkage_method,
                                              algoPrmt.linkage_metric,
                                              algoPrmt.clustering_cutoff_param,
                                              algoPrmt.fcluster_metric)

        self.name_file_drift_plot = compose_name(log_name,
                                              algoPrmt.window_size,
                                              algoPrmt.sliding_window_size,
                                              algoPrmt.linkage_method,
                                              algoPrmt.linkage_metric,
                                              algoPrmt.clustering_cutoff_param,
                                              algoPrmt.fcluster_metric)

    def get_path_input_xes(self):
        return FOLDER_DATA_INITIAL_LOGS / compose_name(self.log_name,XES_FILE_EXTENSION)

    def get_path_input_sorted_xes(self):
        ensure_path_exists(FOLDER_DATA_TIMESTAMP_SORTED_LOGS)
        return FOLDER_DATA_TIMESTAMP_SORTED_LOGS / compose_name(self.log_name, XES_FILE_EXTENSION)

    def get_path_minerful_constraints(self):
        ensure_path_exists(FOLDER_DATA_MINERFUL_DECLARE_CONSTRAINTS)
        return FOLDER_DATA_MINERFUL_DECLARE_CONSTRAINTS / self.namefile_minerful_constr

    def get_path_timestamp_ticks(self):
        ensure_path_exists(FOLDER_TIMESTAMP_TICKS_FOR_GRAPHS)
        return FOLDER_TIMESTAMP_TICKS_FOR_GRAPHS / self.namefile_timestamp_ticks

    def get_path_drift_map(self):
        ensure_path_exists(FOLDER_GRAPHS_DRIFT_MAPS)
        return FOLDER_GRAPHS_DRIFT_MAPS / self.name_file_drift_map

    def get_path_erratic_measures(self):
        ensure_path_exists(FOLDER_GRAPHS_STATISTICS)
        return FOLDER_GRAPHS_STATISTICS / compose_name(self.name_file_erratic, CSV_FILE_EXTENSION)

    def get_path_drift_plot_averaged_timeseries(self, i):
        ensure_path_exists(FOLDER_GRAPHS_DRIFT_AVERAGED_TIMESERIES)
        return FOLDER_GRAPHS_DRIFT_AVERAGED_TIMESERIES / (str(i) + self.name_file_erratic + CSV_FILE_EXTENSION)

    def get_path_drift_plot(self, i):
        ensure_path_exists(FOLDER_GRAPHS_DRIFT_PLOTS_PLOTS)
        return FOLDER_GRAPHS_DRIFT_PLOTS_PLOTS / (str(i) + self.name_file_erratic + PNG_FILE_EXTENSION)

    def get_path_drift_plot_all_timeseries(self, i):
        ensure_path_exists(FOLDER_GRAPHS_DRIFT_ALL_CONSTRAINTS_IN_CLUSTERS)
        return FOLDER_GRAPHS_DRIFT_ALL_CONSTRAINTS_IN_CLUSTERS / (str(i) + self.name_file_erratic + JSON_FILE_EXTENSION)

    def get_path_drift_plot_all_timeseries_pruned(self, i):
        ensure_path_exists(FOLDER_GRAPHS_DRIFT_ALL_CONSTRAINTS_IN_CLUSTERS_PRUNED)
        return FOLDER_GRAPHS_DRIFT_ALL_CONSTRAINTS_IN_CLUSTERS_PRUNED / (str(i) + self.name_file_erratic + CSV_FILE_EXTENSION)

    def get_path_dfg_visualization_for_constraints(self, i):
        ensure_path_exists(FOLDER_GRAPHS_DFG)
        return FOLDER_GRAPHS_DFG / (str(i) + self.name_file_erratic + PNG_FILE_EXTENSION)


class AlgorithmParameters:
    def __init__(self, window_size,
                       sliBy,
                       cluCut,
                       fcluster_metric,
                       linkage_method,
                       linkage_metric,
                       driftAll,
                       noSort,
                       colorTheme,
                       typeConstr):
        self.window_size = window_size
        self.sliding_window_size = sliBy

        self.clustering_cutoff_param = cluCut
        self.fcluster_metric = fcluster_metric
        self.linkage_method = linkage_method
        self.linkage_metric = linkage_metric

        self.change_point_for_all = driftAll
        self.no_sort_in_clusters = noSort

        self.color_theme_drift_map = colorTheme
        self.constraint_type_used = typeConstr


def ensure_path_exists(path):
    if not os.path.exists(path):
        os.makedirs(path)
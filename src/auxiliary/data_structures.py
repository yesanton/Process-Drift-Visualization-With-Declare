import os
from src.auxiliary.simplifiers import compose_name
from src.auxiliary.constant_definitions import FOLDER_DATA_TIMESTAMP_SORTED_LOGS, XES_FILE_EXTENSION, \
    FOLDER_DATA_INITIAL_LOGS, CSV_FILE_EXTENSION, FOLDER_DATA_MINERFUL_DECLARE_CONSTRAINTS, \
    FOLDER_TIMESTAMP_TICKS_FOR_GRAPHS, PNG_FILE_EXTENSION, FOLDER_GRAPHS_DRIFT_MAPS, FOLDER_GRAPHS_STATISTICS, \
    FOLDER_GRAPHS_DRIFT_AVERAGED_TIMESERIES, JSON_FILE_EXTENSION, \
    FOLDER_GRAPHS_DRIFT_ALL_CONSTRAINTS_IN_CLUSTERS, FOLDER_GRAPHS_DRIFT_ALL_CONSTRAINTS_IN_CLUSTERS_PRUNED, \
    FOLDER_GRAPHS_DRIFT_PLOTS_PLOTS, FOLDER_GRAPHS_DFG, FOLDER_DATA_INTERMEDIATE, FOLDER_DATA_RESULTS_FINAL, \
    FOLDER_AUTOCORRELATION


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
        fdtms = FOLDER_DATA_INTERMEDIATE / self.log_name / FOLDER_DATA_TIMESTAMP_SORTED_LOGS
        ensure_path_exists(fdtms)
        return fdtms / compose_name(self.log_name, XES_FILE_EXTENSION)

    def get_path_minerful_constraints(self):
        fdmdc = FOLDER_DATA_INTERMEDIATE / self.log_name / FOLDER_DATA_MINERFUL_DECLARE_CONSTRAINTS
        ensure_path_exists(fdmdc)
        return fdmdc / self.namefile_minerful_constr

    def get_path_timestamp_ticks(self):
        fttfg = FOLDER_DATA_INTERMEDIATE / self.log_name / FOLDER_TIMESTAMP_TICKS_FOR_GRAPHS
        ensure_path_exists(fttfg)
        return fttfg / self.namefile_timestamp_ticks

    def get_path_drift_map(self):
        fgdm = FOLDER_DATA_RESULTS_FINAL / self.log_name / FOLDER_GRAPHS_DRIFT_MAPS
        ensure_path_exists(fgdm)
        return fgdm / self.name_file_drift_map

    def get_path_erratic_measures(self):
        fgs = FOLDER_DATA_RESULTS_FINAL / self.log_name / FOLDER_GRAPHS_STATISTICS
        ensure_path_exists(fgs)
        return fgs / compose_name(self.name_file_erratic, CSV_FILE_EXTENSION)

    def get_path_drift_plot_averaged_timeseries(self, i):
        fgdat = FOLDER_DATA_RESULTS_FINAL / self.log_name / FOLDER_GRAPHS_DRIFT_AVERAGED_TIMESERIES
        ensure_path_exists(fgdat)
        return fgdat / (str(i) + self.name_file_erratic + CSV_FILE_EXTENSION)

    def get_path_drift_plot(self, i):
        fgdpp = FOLDER_DATA_RESULTS_FINAL / self.log_name / FOLDER_GRAPHS_DRIFT_PLOTS_PLOTS
        ensure_path_exists(fgdpp)
        return fgdpp / (str(i) + self.name_file_erratic + PNG_FILE_EXTENSION)

    def get_path_drift_plot_all_timeseries(self, i):
        fgdacic = FOLDER_DATA_RESULTS_FINAL / self.log_name / FOLDER_GRAPHS_DRIFT_ALL_CONSTRAINTS_IN_CLUSTERS
        ensure_path_exists(fgdacic)
        return fgdacic / (str(i) + self.name_file_erratic + JSON_FILE_EXTENSION)

    def get_path_drift_plot_all_timeseries_pruned(self, i):
        fgdacicp = FOLDER_DATA_RESULTS_FINAL / self.log_name / FOLDER_GRAPHS_DRIFT_ALL_CONSTRAINTS_IN_CLUSTERS_PRUNED
        ensure_path_exists(fgdacicp)
        return fgdacicp / (str(i) + self.name_file_erratic + CSV_FILE_EXTENSION)

    def get_path_dfg_visualization_for_constraints(self, i):
        fgd = FOLDER_DATA_RESULTS_FINAL / self.log_name / FOLDER_GRAPHS_DFG
        ensure_path_exists(fgd)
        return fgd / (str(i) + self.name_file_erratic + PNG_FILE_EXTENSION)

    def get_path_autocorrelation_graphs_for_constraints(self, i):
        pat = FOLDER_DATA_RESULTS_FINAL / self.log_name / FOLDER_AUTOCORRELATION
        ensure_path_exists(pat)
        return pat / (str(i) + self.name_file_erratic + PNG_FILE_EXTENSION)

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
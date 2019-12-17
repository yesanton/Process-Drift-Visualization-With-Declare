import os
from pathlib import Path

from pathlib import Path

ROOT_DIR =  Path(__file__).parent.parent.parent # This is your Project Root

FOLDER_DATA_INITIAL_LOGS = Path(ROOT_DIR) / 'data' / 'data_initial'
FOLDER_DATA_TIMESTAMP_SORTED_LOGS = Path(ROOT_DIR) / 'data' / "data_intermediate" / "timestamp_sorted_logs"

FOLDER_DATA_MINERFUL_DECLARE_CONSTRAINTS = Path(ROOT_DIR) / 'data' / "data_intermediate" / "declare_from_minerful"
FOLDER_TIMESTAMP_TICKS_FOR_GRAPHS = Path(ROOT_DIR) / 'data' / "data_intermediate" / "timestamp_ticks_for_graphs"

FOLDER_GRAPHS_DRIFT_MAPS = Path(ROOT_DIR) / 'data' / "data_results_final" / "graphs" / "drift_maps"
FOLDER_GRAPHS_DRIFT_PLOTS = Path(ROOT_DIR) / 'data' / "data_results_final" / "graphs" / "drift_plots"
FOLDER_GRAPHS_STATISTICS = Path(ROOT_DIR) / 'data' / "data_results_final" / "statistics"

FOLDER_CONSTRAINTS_IN_CLUSTERS = Path(ROOT_DIR) / 'data' / "data_intermediate" / "constraints_in_clusters"

XES_FILE_EXTENSION = '.xes'
CSV_FILE_EXTENSION = '.csv'
PNG_FILE_EXTENSION = '.png'
NAME_FILE_SEPARATOR = '_'
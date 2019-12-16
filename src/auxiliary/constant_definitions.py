import os
from pathlib import Path

from pathlib import Path

ROOT_DIR =  Path(__file__).parent.parent.parent # This is your Project Root

DATA_INITIAL_LOGS_FOLDER = Path(ROOT_DIR) / 'data'/ 'data_initial'
DATA_TIMESTAMP_SORTED_LOGS_FOLDER = Path(ROOT_DIR) / 'data'/ "data_intermediate" / "timestamp_sorted_logs"


DATA_MINERFUL_DECLARE_CONSTRAINTS_FOLDER = Path(ROOT_DIR) / 'data'/ "data_intermediate" / "declare_from_minerful"
TIMESTAMP_TICKS_FOR_GRAPHS_FOLDER = Path(ROOT_DIR) / 'data'/ "data_intermediate" / "timestamp_ticks_for_graphs"

XES_FILE_EXTENSION = '.xes'
CSV_FILE_EXTENSION = '.csv'
NAME_FILE_SEPARATOR = '_'
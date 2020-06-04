''' main script for the algorithm execution
Example run:
python3 draw_graph.py -logName bpi_challenge_2013_open  -subL 100 -sliBy 50 -driftAll
call help to see argument list

examples to run:
-logName bpi_challenge_2013_incidents -subL 400 -sliBy 150 -cluCut 500
-logName Sepsis -subL 50 -sliBy 25 -cluCut 600
-logName ConditionalRemoval -subL 1000 -sliBy 500  -cluCut 600
-logName Loop -subL 800 -sliBy 400  -cluCut 600
-logName italian_help_desk -subL 200  -sliBy 75  -cluCut 300
-logName OIR -subL 400  -sliBy 200  -cluCut 500
-logName bpic_2011_hospital -subL 40 -sliBy 20 -cluCut 1200 <<<<<<---
-logName bpic_2011_hospital -subL 100 -sliBy 50 -cluCut 1200
-logName bastian -subL 100 -sliBy 50 -cluCut 1200
Author:  Anton Yeshchenko
'''
import json

from src.auxiliary.web_parameters import get_http_parameters
from src.agregated_functions import process_constraint_clusters
from src.auxiliary.mine_features_from_data import save_separately_timestamp_for_each_constraint_window
from src.data_algorithms_cluster_and_change_point import do_cluster_changePoint
from src.auxiliary.command_line import get_commandline_parameters
from src.visualize_drift_map import draw_drift_map_with_clusters
from src.data_exporters.export_csv import export_one_line_csvs
from src.data_exporters.export_xes import export_xes_log
from src.data_importers.import_csv import import_timestamp_ticks, import_check, import_minerful_constraints_timeseries_data
from src.data_importers.import_xes import import_xes_and_sort_timestamp, import_xes
from src.auxiliary.minerful_adapter import mine_minerful_for_declare_constraints

# make this add to be able to run on the server with Flask
from flask import Flask, request
import flask
app = Flask(__name__, static_url_path='/data/', static_folder='../data/')
import os
dir_path = os.path.dirname(os.path.realpath(__file__))




@app.route('/buildDriftMap', methods=['GET'])
def run_scenario1():
    # post_id = request.args.get('id')
    # return post_id

    # this is for working with command line
    # fileMngm, algoPrmts = get_commandline_parameters()

    # and this is added instead of the previous lines to work with web version with requests
    fileMngm, algoPrmts = get_http_parameters(request.args)

    log = import_xes(fileMngm)
    if not log:
        log = import_xes_and_sort_timestamp(fileMngm)
        export_xes_log(log, fileMngm)

    if not import_check(fileMngm.get_path_minerful_constraints()):
        mine_minerful_for_declare_constraints(fileMngm, algoPrmts)

    ts_ticks = import_timestamp_ticks(fileMngm)
    if not ts_ticks:
        ts_ticks = save_separately_timestamp_for_each_constraint_window(log, algoPrmts)
        export_one_line_csvs(ts_ticks, fileMngm.get_path_timestamp_ticks())

    constraints = import_minerful_constraints_timeseries_data(fileMngm, algoPrmts)

    constraints, \
    cluster_bounds, \
    horisontal_separation_bounds_by_cluster, \
    clusters_with_declare_names, \
    clusters_dict, \
    cluster_order = \
        do_cluster_changePoint(constraints, algoPrmts)

    print("- - - start drawing drift map" )
    draw_drift_map_with_clusters(constraints,
                                 fileMngm,
                                 algoPrmts,
                                 ts=ts_ticks,
                                 y_lines=cluster_bounds,
                                 x_lines_all=horisontal_separation_bounds_by_cluster,
                                 cluster_order = cluster_order)

    print("- - - start processing the timeseries in clusters" )
    # handle now each cluster of constraints in the following function
    process_constraint_clusters(fileMngm,
                                cluster_order,
                                clusters_with_declare_names,
                                ts_ticks,
                                clusters_dict,
                                horisontal_separation_bounds_by_cluster,
                                erratic_measure_out = True,
                                export_constraints = True,
                                export_constraints_simplified = True)



    # return flask.url_for('static', filename='results/README.md')

    # jsonStr = json.dumps(fileMngm.__dict__)
    at = []
    for i in range(len(cluster_order)):
        at.append(str(fileMngm.get_path_drift_plot_averaged_timeseries_URL(i)))




    return flask.jsonify(path_to_driftmap=str(fileMngm.get_path_drift_map_URL()),
                         path_to_erratic_measure=str(fileMngm.get_path_erratic_measures_URL()),
                         paths_to_drift_plots=at)

''' main script for the algorithm execution with a server

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
from statistics import mean

from src.auxiliary.web_parameters import get_http_parameters
from src.agregated_functions import process_constraint_clusters
from src.auxiliary.mine_features_from_data import save_separately_timestamp_for_each_constraint_window
from src.data_algorithms_cluster_and_change_point import do_cluster_changePoint, remove_redundant_timeseries_HEADER
from src.auxiliary.command_line import get_commandline_parameters
from src.visualize_drift_map import draw_drift_map_with_clusters
from src.data_exporters.export_csv import export_one_line_csvs
from src.data_exporters.export_xes import export_xes_log
from src.data_importers.import_csv import import_timestamp_ticks, import_check, import_minerful_constraints_timeseries_data
from src.data_importers.import_xes import import_xes_and_sort_timestamp, import_xes
from src.auxiliary.minerful_adapter import mine_minerful_for_declare_constraints
from src.visualize_autocorrelation_plots import visualize_autocorrelation_plots
from src.auxiliary.command_line import get_commandline_parameters
from src.visualize_dfg_with_constraints import visualize_dfg_with_constraints


import csv
import numpy as np
from statsmodels.tsa.stattools import adfuller
# https://machinelearningmastery.com/time-series-data-stationary-python/
from src.data_importers.import_csv import import_check


# make this add to be able to run on the server with Flask
from flask import Flask, request
import flask


app = Flask(__name__, static_url_path='/data/', static_folder='../data/')
import os
dir_path = os.path.dirname(os.path.realpath(__file__))

@app.route('/makeDriftMap', methods=['GET'])
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





@app.route('/makeEDFG', methods=['GET'])
def run_scenario2_eDFG():
    fileMngm, algoPrmts = get_http_parameters(request.args)
    visualize_dfg_with_constraints(fileMngm)


    #now here saving and sending back the links to these visualizations
    curr_ind = 0
    at = []
    while import_check(fileMngm.get_path_drift_plot_all_timeseries_pruned(curr_ind)):

        at.append(fileMngm.get_path_dfg_visualization_for_constraints_URL(curr_ind))

    return flask.jsonify(paths_to_edfgs=at)


@app.route('/makeAutocorrelationPlots', methods=['GET'])
def run_scenario3_autocorrelation():
    fileMngm, algoPrmts = get_commandline_parameters()
    visualize_autocorrelation_plots(fileMngm)

@app.route('/makeStationarityTest', methods=['GET'])
def run_scenario4_stationarity():
    fileMngm, algoPrmts = get_commandline_parameters()

    curr_ind = 0
    while import_check(fileMngm.get_path_drift_plot_averaged_timeseries(curr_ind)):
        b = []

        with open(fileMngm.get_path_drift_plot_averaged_timeseries(curr_ind)) as save_time_series_per_cl:
            r = csv.reader(save_time_series_per_cl, dialect='excel')
            for a in r:
                for i in a:
                    b.append(float(i))
        X = np.array(b)

        result = adfuller(X)

        print("Data number " + str(curr_ind))
        print('ADF Statistic: %f' % result[0])
        print('p-value: %f' % result[1])
        print('Critical Values:')
        for key, value in result[4].items():
            print('\t%s: %.3f' % (key, value))

        curr_ind += 1


@app.route('/makeSpreadOfConstraints', methods=['GET'])
def run_scenario5_spread():
    fileMngm, algoPrmts = get_commandline_parameters()

    constraints = import_minerful_constraints_timeseries_data(fileMngm, algoPrmts)
    constraints = remove_redundant_timeseries_HEADER(constraints)

    measure = mean([max(co[3:]) - min(co[3:]) for co in constraints])
    print("average spread of all measures: " + str(measure))


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

to run it locally use these:
    $ export FLASK_APP=scenarios_server.py
    $ export FLASK_ENV=development
    $ flask run
'''
import json
from statistics import mean
from werkzeug.utils import secure_filename
from src.auxiliary.web_server_functions import clean_from_old_files
from src.auxiliary.data_structures import FilesManagement
from src.auxiliary.web_parameters import get_http_parameters, get_possible_args
from src.agregated_functions import process_constraint_clusters
from src.auxiliary.mine_features_from_data import save_separately_timestamp_for_each_constraint_window
from src.data_algorithms_cluster_and_change_point import do_cluster_changePoint, remove_redundant_timeseries_HEADER
from src.auxiliary.command_line import get_commandline_parameters
from src.visualize_drift_map import draw_drift_map_with_clusters
from src.data_exporters.export_csv import export_one_line_csvs, export_many_line_csvs
from src.data_exporters.export_xes import export_xes_log
from src.data_importers.import_csv import import_timestamp_ticks, import_check, import_minerful_constraints_timeseries_data
from src.data_importers.import_xes import import_xes_and_sort_timestamp, import_xes
from src.auxiliary.minerful_adapter import mine_minerful_for_declare_constraints
from src.visualize_autocorrelation_plots import visualize_autocorrelation_plots
from src.auxiliary.command_line import get_commandline_parameters
from src.visualize_dfg_with_constraints import visualize_dfg_with_constraints
import os
import uuid
import csv
import numpy as np
from statsmodels.tsa.stattools import adfuller
# https://machinelearningmastery.com/time-series-data-stationary-python/
from src.data_importers.import_csv import import_check
from pathlib import Path

# make this add to be able to run on the server with Flask
from flask import Flask, request
import flask
from flask_cors import CORS, cross_origin

# os.environ['PATH'] = os.environ['PATH']+os.pathsep+r"/usr/local/lib/python3.8/dist-packages/graphviz"
# '/usr/local/lib/python3.8/dist-packages/graphviz'

app = Flask(__name__, static_url_path='/data/', static_folder='../data/')
# enable resource sharing
cors = CORS(app, resources={r"/*": {"origins": "*"}})
# CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'
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
        at.append(fileMngm.get_path_drift_plot_URL(i))




    return flask.jsonify(path_to_driftmap=fileMngm.get_path_drift_map_URL(),
                         path_to_erratic_measure=fileMngm.get_path_erratic_measures_URL(),
                         paths_to_drift_plots=at)





@app.route('/makeEDFG', methods=['GET'])
def run_scenario2_eDFG():
    fileMngm, algoPrmts = get_http_parameters(request.args)
    visualize_dfg_with_constraints(fileMngm)

    print ("done making graphs")

    #now here saving and sending back the links to these visualizations
    curr_ind = 0
    at = []
    while import_check(fileMngm.get_path_drift_plot_all_timeseries_pruned(curr_ind)):
        at.append(fileMngm.get_path_dfg_visualization_for_constraints_URL(curr_ind))
        curr_ind += 1
    return flask.jsonify(paths_to_edfgs=at)


@app.route('/makeAutocorrelationPlots', methods=['GET'])
def run_scenario3_autocorrelation():
    fileMngm, algoPrmts = get_http_parameters(request.args)
    visualize_autocorrelation_plots(fileMngm)

    # now here saving and sending back the links to these visualizations
    curr_ind = 0
    at = []
    while import_check(fileMngm.get_path_drift_plot_averaged_timeseries(curr_ind)):
        at.append(fileMngm.get_path_autocorrelation_graphs_for_constraints_URL(curr_ind))
        curr_ind += 1
    return flask.jsonify(paths_to_autocorrelation=at)



# example:
#         http://127.0.0.1:5000/makeStationarityTest?logName=Sepsis&subL=100&sliBy=50
@app.route('/makeStationarityTest', methods=['GET'])
def run_scenario4_stationarity():
    fileMngm, algoPrmts = get_http_parameters(request.args)
    export = [['cluster','ADF Statistic', 'p-value', '1%', '5%', '10%']]
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
        export_1 = []
        export_1.append(curr_ind)
        print("Data number " + str(curr_ind))
        export_1.append(result[0])
        print('ADF Statistic: %f' % result[0])
        export_1.append(result[1])
        print('p-value: %f' % result[1])
        print('Critical Values:')
        for key, value in result[4].items():
            print('\t%s: %.3f' % (key, value))
            export_1.append(value)
        curr_ind += 1
        export.append(export_1)

    print (export)
    export_many_line_csvs(export, fileMngm.get_path_stationarity())

    return flask.jsonify(path_to_stationarity=fileMngm.get_path_stationarity_URL())




@app.route('/makeSpreadOfConstraints', methods=['GET'])
def run_scenario5_spread():
    fileMngm, algoPrmts = get_http_parameters(request.args)

    constraints = import_minerful_constraints_timeseries_data(fileMngm, algoPrmts)
    constraints = remove_redundant_timeseries_HEADER(constraints)

    measure = mean([max(co[3:]) - min(co[3:]) for co in constraints])
    print("average spread of all measures: " + str(measure))

    return flask.jsonify(spread_constraints=measure)


# uploading the event log
# documentation:
# https://flask.palletsprojects.com/en/1.1.x/patterns/fileuploads/#uploading-files
# and short version: https://flask.palletsprojects.com/en/1.1.x/quickstart/#static-files
UPLOAD_FOLDER = FilesManagement.get_path_uploading_file()
ALLOWED_EXTENSIONS = {'xes'}

STORAGE_MAX_GB = os.getenv("MEMORY_LIMIT")
if not STORAGE_MAX_GB:
    # todo change this
    STORAGE_MAX_GB = 100
# storage preserved for a possible analysis in this session. 1 gb is an adequate estimate for all possible things.
STORAGE_PRESERVED = 1


@app.route('/uploadFile', methods=['GET', 'POST'])
# @cross_origin()
def upload_event_log():
    # function to check if the file is in allowed format
    def allowed_file(filename):
        return '.' in filename and \
               filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


    # cleaning up space in the data folder if necessary
    root_directory = Path(FilesManagement.get_path_all_data())

    def sizeof_fmt(num, suffix='B'):
        for unit in ['', 'Ki', 'Mi', 'Gi', 'Ti', 'Pi', 'Ei', 'Zi']:
            if abs(num) < 1024.0:
                return "%3.1f%s%s" % (num, unit, suffix)
            num /= 1024.0
        return "%.1f%s%s" % (num, 'Yi', suffix), num

    memory_taken_by_data_files = sum(f.stat().st_size for f in root_directory.glob('**/*') if f.is_file())

    print('Storage occupied by data           : ' + sizeof_fmt(memory_taken_by_data_files))
    print('Storage preserved for new analysis : ' + str(STORAGE_PRESERVED))
    print('Storage limit                      : ' + str(STORAGE_MAX_GB))

    while (memory_taken_by_data_files / 1073741824 + STORAGE_PRESERVED) > STORAGE_MAX_GB: # also changed to gb (and add one more gb for a newly uploading file)
        print('Storage to free                    : ' + str(memory_taken_by_data_files / 1073741824 + STORAGE_PRESERVED - STORAGE_MAX_GB) + ' GiB')
        clean_from_old_files()
        memory_taken_by_data_files1 = sum(f.stat().st_size for f in root_directory.glob('**/*') if f.is_file())
        print('Storage occupied by data           : ' + sizeof_fmt(memory_taken_by_data_files1))
        memory_taken_by_data_files = memory_taken_by_data_files1


    print('Importing a new file')
    if request.method == 'POST':
        f = request.files['file']
        print (f.filename)
        if allowed_file(f.filename):
            unique_id = str(uuid.uuid1())
            filename_no_ext = f.filename[:len(f.filename)-4]
            if len(filename_no_ext) > 25:
                new_file_name = filename_no_ext[:25] + '_' + unique_id
            else:
                new_file_name = filename_no_ext + '_' + unique_id

            f.save(UPLOAD_FOLDER / secure_filename(new_file_name + '.xes'))
            print('returning json now with id: ' + str(secure_filename(new_file_name + '.xes')))
            # return flask.jsonify(session_id=unique_id)
            # response = app.response_class(
            #     response=json.dumps({"session_id": new_file_name}),
            #     status=200,
            #     mimetype='application/json'
            # )

            #get recommended parameteres
            _, algoPrmts = get_http_parameters(request.args)
            fm = FilesManagement(secure_filename(new_file_name), algoPrmts)
            d = fm.get_path_input_xes()
            # print (' d : ' + str(d))

            # return flask.jsonify(session_id=new_file_name)
            return get_possible_args(secure_filename(new_file_name), d)
        else:
            # The HTTP 415 Unsupported Media Type client error response code indicates that the server refuses
            # to accept the request because the payload format is in an unsupported format.
            return 'File format is not allowed, it should be .xes instead', 415

    return "Is was it a POST request?", 400
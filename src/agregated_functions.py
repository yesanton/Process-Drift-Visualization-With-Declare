import csv

from src.auxiliary.constant_definitions import FOLDER_GRAPHS_STATISTICS, CSV_FILE_EXTENSION, FOLDER_GRAPHS_DRIFT_PLOTS, \
    FOLDER_CONSTRAINTS_IN_CLUSTERS
from src.auxiliary.simplifiers import compose_name
from src.data_algorithms import calculate_erratic_value
from src.data_exporters.export_csv import export_one_line_csvs
from src.data_exporters.export_json import export_constraints_per_cluster
from src.draw_drift_plot import draw_drift_plot_for_one_cluster

#TODO implement these:
# erratic_measure_out = True,
#         drift_plots = True,
#         export_constraints = True,
#         export_constraints_simplified = True
def process_constraints(
        cluster_order,
        dataset_name,tStart,subL, sliBy, append_name,clusters_with_declare_names,file_name_out,ts,clusters_dict,horisontal_separation_bounds_by_cluster,
        erratic_measure_out = True,
        drift_plots = True,
        export_constraints = True,
        export_constraints_simplified = True):
    # save erratic measure measurements

    erratic_output = FOLDER_GRAPHS_STATISTICS / compose_name(dataset_name, tStart, subL, sliBy, append_name,
                                                             CSV_FILE_EXTENSION)
    writeErraticFile = open(erratic_output, 'w')
    writerErratic = csv.writer(writeErraticFile)
    writerErratic.writerow(["Cluster number", "Erratic measure without drift", "Erratic measure of the cluster"])

    # draw for each cluster results and write to file
    for i, j in zip(cluster_order, range(len(cluster_order))):
        # todo this is to the import folder
        # output the declare constraints in the good format for minerful to draw
        export_constraints_per_cluster(clusters_with_declare_names[i],
                                       save_name=file_name_out[:-4] + 'cl-' + str(j) + '.json',
                                       logFolder=FOLDER_CONSTRAINTS_IN_CLUSTERS)

        power_smooth, xnew, averaged_line = draw_drift_plot_for_one_cluster(ts=ts,
                                                                               clusters_dict=clusters_dict, key=i,
                                                                               vertical=horisontal_separation_bounds_by_cluster,
                                                                               name_save=file_name_out[
                                                                                         :-4] + 'cl-' + str(j) + '.png',
                                                                               logFolder=FOLDER_GRAPHS_DRIFT_PLOTS)

        new_path = FOLDER_GRAPHS_DRIFT_PLOTS / 'timeseries'
        export_one_line_csvs(averaged_line, compose_name((file_name_out[:-4] + 'cl-' + str(j)), '.csv'), new_path)


        standard_erratic, real_erratic_score = calculate_erratic_value(power_smooth, xnew, averaged_line)
        writerErratic.writerow([j, standard_erratic, real_erratic_score])


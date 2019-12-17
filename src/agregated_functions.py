import csv

from src.auxiliary.constant_definitions import FOLDER_GRAPHS_DRIFT_PLOTS, \
    FOLDER_GRAPHS_DRIFT_ALL_CONSTRAINTS_IN_CLUSTERS
from src.data_algorithms import calculate_erratic_value
from src.data_exporters.export_csv import export_one_line_csvs
from src.data_exporters.export_json import export_constraints_per_cluster
from src.draw_drift_plot import draw_drift_plot_for_one_cluster

#TODO implement these:
# erratic_measure_out = True,
#         drift_plots = True,
#         export_constraints = True,
#         export_constraints_simplified = True
def process_constraints(fileMngm,
                        cluster_order,
                        clusters_with_declare_names,
                        ts_ticks,
                        clusters_dict,
                        horisontal_separation_bounds_by_cluster,
                        erratic_measure_out = True,
                        drift_plots = True,
                        export_constraints = True,
                        export_constraints_simplified = True):

    # save erratic measure measurements
    writeErraticFile = open(fileMngm.get_path_erratic_measures(), 'w')
    writerErratic = csv.writer(writeErraticFile)
    writerErratic.writerow(["Cluster number", "Erratic measure without drift", "Erratic measure of the cluster"])

    # draw for each cluster results and write to file
    for i, j in zip(cluster_order, range(len(cluster_order))):
        # todo this is to the import folder
        # output the declare constraints in the good format for minerful to draw

        # todo remove last argument
        export_constraints_per_cluster(clusters_with_declare_names[i],
                                       save_name=fileMngm.get_path_drift_plot_all_timeseries(j),
                                       logFolder=FOLDER_GRAPHS_DRIFT_ALL_CONSTRAINTS_IN_CLUSTERS)

        power_smooth, \
        xnew, \
        averaged_line = draw_drift_plot_for_one_cluster(ts=ts_ticks,
                                                        clusters_dict=clusters_dict,
                                                        key=i,
                                                        vertical=horisontal_separation_bounds_by_cluster,
                                                        name_save=fileMngm.get_path_drift_plot(j),
                                                        logFolder=FOLDER_GRAPHS_DRIFT_PLOTS)


        export_one_line_csvs(averaged_line,
                             fileMngm.get_path_drift_plot_averaged_timeseries(j))

        standard_erratic, real_erratic_score = calculate_erratic_value(power_smooth, xnew, averaged_line)
        writerErratic.writerow([j, standard_erratic, real_erratic_score])


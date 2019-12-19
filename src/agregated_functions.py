from src.auxiliary.minerful_adapter import prune_constraints_minerful
from src.data_algorithms_cluster_and_change_point import calculate_erratic_value
from src.data_exporters.export_csv import export_one_line_csvs, export_many_line_csvs
from src.data_exporters.export_json import export_constraints_per_cluster
from src.visualize_drift_plot import draw_drift_plot_for_one_cluster

def process_constraint_clusters(fileMngm,
                                cluster_order,
                                clusters_with_declare_names,
                                ts_ticks,
                                clusters_dict,
                                horisontal_separation_bounds_by_cluster,
                                erratic_measure_out = True,
                                export_constraints = True,
                                export_constraints_simplified = True):

    # save erratic measure measurements
    erratic = []
    erratic.append(["Cluster number", "Erratic measure without drift", "Erratic measure of the cluster"])

    # draw for each cluster results and write to file
    for i, j in zip(cluster_order, range(len(cluster_order))):

        # output the declare constraints in the good format for minerful to draw
        if export_constraints:
            export_constraints_per_cluster(clusters_with_declare_names[i],
                                       fileMngm=fileMngm, file_ind=j)

        # prune constraints after we record full constraints to the file
        if export_constraints_simplified:
            prune_constraints_minerful(fileMngm, file_ind=j)

        power_smooth, \
        xnew, \
        averaged_line = draw_drift_plot_for_one_cluster(ts=ts_ticks,
                                                        clusters_dict=clusters_dict,
                                                        key=i,
                                                        vertical=horisontal_separation_bounds_by_cluster,
                                                        file_ind=j,
                                                        fileMngm = fileMngm)

        # export here the timeseries from each cluster
        export_one_line_csvs(averaged_line,
                             fileMngm.get_path_drift_plot_averaged_timeseries(j))

        standard_erratic, real_erratic_score = calculate_erratic_value(power_smooth, xnew, averaged_line)
        erratic.append([j, standard_erratic, real_erratic_score])

    if erratic_measure_out:
        export_many_line_csvs(erratic, fileMngm.get_path_erratic_measures())
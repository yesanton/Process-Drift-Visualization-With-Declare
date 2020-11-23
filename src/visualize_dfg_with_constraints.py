from pm4py.objects.log.importer.xes import factory as xes_import_factory
from pm4py.algo.discovery.heuristics import factory as heuristics_miner
from pm4py.visualization.heuristics_net import factory as hn_vis_factory
import src.pm4py_modified_scripts.factory_pm4py as  hn_vis_factory
from src.data_importers.import_csv import import_check, import_constraints_to_dictionary, import_erratic_measures


# from src.auxiliary.data_structures import FilesManagement

def visualize_dfg_with_constraints(fileMngm):
    # import log
    log = xes_import_factory.apply(str(fileMngm.get_path_input_sorted_xes()))
    print ('dfg -- xes is imported')
    # bpi 2011 specific (experiment)
    #heu_net = heuristics_miner.apply_heu(log, parameters={"dependency_thresh": 0.99, "min_act_count":5000})

    # this is usual
    # heu_net = heuristics_miner.apply_heu(log, parameters={"dependency_thresh": 0.99})

    # now for the specific experiment bbb
    heu_net = heuristics_miner.apply_heu(log, parameters={"dependency_thresh": 0.5, "min_act_count": 500, 'min_dfg_occurrences': 500})
    print ('dfg -- heuristic miner is done')


    curr_ind = 0

    # import erratic measure to calculate what needs to be visualized
    erratic = import_erratic_measures(fileMngm.get_path_erratic_measures())
    max_err = max (erratic)
    min_err = min (erratic)
    scale = max_err / min_err

    while import_check(fileMngm.get_path_drift_plot_all_timeseries_pruned(curr_ind)):
        if (scale / (max_err / erratic[curr_ind])) > 1.3:
            # input the constraints from the file here
            constraints = import_constraints_to_dictionary(
                fileMngm.get_path_drift_plot_all_timeseries_pruned(curr_ind))

            gviz = hn_vis_factory.apply_with_constraints(heu_net, constr=constraints)
            # hn_vis_factory.view(gviz)

            hn_vis_factory.save(gviz,fileMngm.get_path_dfg_visualization_for_constraints(curr_ind))
        curr_ind += 1
        print('dfg -- current plot index: ' + str(curr_ind))

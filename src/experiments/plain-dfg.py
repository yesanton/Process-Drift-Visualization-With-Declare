from pm4py.objects.log.importer.xes import factory as xes_import_factory
import os

from pm4py.objects.log.importer.xes import factory as xes_importer
log = xes_importer.import_log('../../data/data_input/italian_help_desk.xes')

from pm4py.algo.discovery.dfg import factory as dfg_factory
dfg = dfg_factory.apply(log)

from pm4py.visualization.dfg import factory as dfg_vis_factory
gviz = dfg_vis_factory.apply(dfg, log=log, variant="frequency")
dfg_vis_factory.view(gviz)
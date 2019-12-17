from pm4py.objects.log.exporter.xes import factory as xes_exporter

def export_xes_log(log, fileMngm):
    xes_exporter.export_log(log, str(fileMngm.get_path_input_sorted_xes()))


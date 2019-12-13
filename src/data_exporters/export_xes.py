from pm4py.objects.log.exporter.xes import factory as xes_exporter

def export_xes_log(log, folder_name, name_file):
    xes_exporter.export_log(log, str(folder_name / name_file))
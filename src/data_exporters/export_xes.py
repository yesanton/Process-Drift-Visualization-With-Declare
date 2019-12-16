from pm4py.objects.log.exporter.xes import factory as xes_exporter

def export_xes_log(log, name_file, folder_name):
    xes_exporter.export_log(log, str(folder_name / name_file))


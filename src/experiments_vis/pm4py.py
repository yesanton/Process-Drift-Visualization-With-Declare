from pm4py.objects.log.importer.xes import factory as xes_import_factory


event_log = "data_input/italian_help_desk/italian_help_desk.xes"

log = xes_import_factory.apply(event_log)


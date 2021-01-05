from pm4py.objects.log.importer.xes import importer as xes_import_factory

def import_xes_and_sort_timestamp(fileMngm):
    full_path_file = fileMngm.get_path_input_xes()

    if not full_path_file.is_file():
        raise FileNotFoundError('File is not found at ' + str(full_path_file))

    parameters = {"timestamp_sort": True}
    return xes_import_factory.apply(str(full_path_file), parameters=parameters)

def import_xes(fileMngm):
    if not fileMngm.get_path_input_sorted_xes().is_file():
        return None
    return xes_import_factory.apply(str(fileMngm.get_path_input_sorted_xes()))


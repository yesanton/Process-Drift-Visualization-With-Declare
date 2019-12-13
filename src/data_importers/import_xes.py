from pathlib import Path

from pm4py.objects.log.importer.xes import factory as xes_import_factory


def import_xes_and_sort_timestamp(folder_file, name_file):
    full_path_file = folder_file / name_file

    if not full_path_file.is_file():
        raise FileNotFoundError('File is now found at ' + str(full_path_file))

    parameters = {"timestamp_sort": True}
    return xes_import_factory.apply(str(full_path_file), parameters=parameters)

def import_xes(folder_file, name_file):
    full_path_file = folder_file / name_file

    if not full_path_file.is_file():
        return None

    return xes_import_factory.apply(str(full_path_file))


from pathlib import Path

from pm4py.objects.log.importer.xes import factory as xes_import_factory

from src.auxiliary.data_structures import FilesManagement


def import_xes_and_sort_timestamp(fileMngm):
    full_path_file = fileMngm.get_path_input_xes()

    if not full_path_file.is_file():
        raise FileNotFoundError('File is now found at ' + str(full_path_file))

    parameters = {"timestamp_sort": True}
    return xes_import_factory.apply(str(full_path_file), parameters=parameters)

def import_xes(fileMngm):
    if isinstance(fileMngm, FilesManagement):
        file_path = fileMngm.get_path_input_sorted_xes()
    else:
        file_path = Path(fileMngm)

    print (file_path)
    if not file_path.is_file():
        return None
    return xes_import_factory.apply(str(file_path))
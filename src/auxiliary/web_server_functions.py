'''this file contains methods that are important for maintaining the normal
functioning of the flask server based on this repository

'''
import datetime
import pathlib

from src.auxiliary.data_structures import FilesManagement


def clean_from_old_files():
    # find oldest file in 'data_input'
    # find all folders containing the results for this file in 'data'
    # clean everything up
    files_py = pathlib.Path(FilesManagement.get_path_uploading_file()).glob("*.xes")
    files = [x for x in files_py if x.is_file()]

    remember_file_with_the_first_date = files[0]
    min_date = files[0].stat().st_mtime
    for f in files:
        # date created - st_ctime
        # date modified - st_mtime
        print (f,datetime.datetime.fromtimestamp(f.stat().st_mtime))

        if min_date > f.stat().st_mtime:
            min_date = f.stat().st_mtime
            remember_file_with_the_first_date = f

    # TODO delete all files of the first
    print ('removing all additional files connected to the ' + str(remember_file_with_the_first_date))



    return 'Success cleaning XXX file\nNNN memory was cleaned up'
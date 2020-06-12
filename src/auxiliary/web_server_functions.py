'''this file contains methods that are important for maintaining the normal
functioning of the flask server based on this repository

'''
import datetime
import os
import pathlib
import shutil

from src.auxiliary.data_structures import FilesManagement


def clean_from_old_files():
    # find oldest file in 'data_input'
    # find all folders containing the results for this file in 'data'
    # clean everything up

    # 1. find oldest file
    files_py = pathlib.Path(FilesManagement.get_path_uploading_file()).glob("*.xes")
    files = [x for x in files_py if x.is_file()]

    remember_file_with_the_first_date = files[0]
    min_date = files[0].stat().st_mtime
    for f in files:
        # date created - st_ctime
        # date modified - st_mtime
        # uncomment this to see all files with their date in the console
        # print (f,datetime.datetime.fromtimestamp(f.stat().st_mtime))

        if min_date > f.stat().st_mtime:
            min_date = f.stat().st_mtime
            remember_file_with_the_first_date = f

    # 2. delete all related files of to the oldest file
    name = remember_file_with_the_first_date.stem
    print('Removing associated files to       : ' + str(name))

    delete_folder_1 = FilesManagement.get_path_data_intermediate() / name
    print ('Removing folder                    : ' + str(delete_folder_1))
    try:
        shutil.rmtree(delete_folder_1)
    except:
        print('Error while deleting directory')

    delete_folder_2 = FilesManagement.get_path_data_results_final() / name
    print('Removing folder                    : ' + str(delete_folder_2))
    try:
        shutil.rmtree(delete_folder_2)
    except:
        print('Error while deleting directory')
    print ("Removing the main input file       : " + name)
    if os.path.isfile(remember_file_with_the_first_date):
        # os.remove(remember_file_with_the_first_date)
        remember_file_with_the_first_date.unlink()
    else:  ## Show an error ##
        print("Error: %s file not found" % remember_file_with_the_first_date)


    print ('Success cleaning everything associated with ' + name +  ' file')
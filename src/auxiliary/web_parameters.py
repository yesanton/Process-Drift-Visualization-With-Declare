'''
This script is used when the app will be used with the command line arguments
to parse and understand them
Example run:
python3 draw_graph.py -logName bpi_challenge_2013_open -subL 100 -sliBy 50  -driftAll

call help to see argument list
Author:  Anton Yeshchenko
'''
# lib documentation
# https://pymotw.com/2/argparse/
import argparse
from src.auxiliary.data_structures import FilesManagement, AlgorithmParameters

def get_http_parameters(args):
    # return (args.get('logName'))

    logName = args.get('logName')
    if not logName:
        logName = "italian_help_desk"

    subL = args.get('subL')
    if not subL:
        subL = 100
    subL = int(subL)

    sliBy = args.get('sliBy')
    if not sliBy:
        sliBy = 50
    sliBy = int(sliBy)
# http://127.0.0.1:5000/?logName=gdfgdfgdfg&subL=100&sliBy=50&cluCut=300&&&&&&&

    # Cutoff threshold for cluster algorithm
    cluCut = args.get('cluCut')
    if not cluCut:
        cluCut = 300
    cluCut = int(cluCut)


    # 'set this optional parameter if you want to generale change points for the whole set at '
    # 'the same time (if not set, every cluster will get its own changepoint)'
    driftAll = args.get('driftAll')
    if not driftAll:
        driftAll = False
    else:
        driftAll = True

    # set this optional parameter if the constrains shouldn\'t be sorted inside of clusters
    noSort = args.get('noSort')
    if not driftAll:
        noSort = False
    else:
        noSort = True

    # set the option for the colors of the Drift Map, the option can be found '
    # 'https://matplotlib.org/users/colormaps.html, we recommend \'plasma\' or \'PiYG\' or \'bw\''
    colorTheme = args.get('colorTheme')
    if not colorTheme:
        colorTheme = "plasma"

    # "\'support\', \'confidence\' or \'interestFactor\
    typeConstr = args.get('typeConstr')
    if not typeConstr:
        typeConstr = 'confidence'

    # parser = argparse.ArgumentParser()
    # These are the argument list  of the import subprocess script
    # parser.add_argument("-logName", help="the log name", default="italian_help_desk")
    # parser.add_argument("-subL", type=int, default=100,help="Window size for slicing the log")
    # parser.add_argument("-sliBy", type=int, default=50)
    # parser.add_argument("-cluCut", type=int, default=300, help="Cutoff threshold for cluster algorithm")
    # parser.add_argument('-driftAll', action='store_true', default=False,
    #                     dest='driftAll',
    #                     help='set this optional parameter if you want to generale change points for the whole set at '
    #                          'the same time (if not set, every cluster will get its own changepoint)')
    # parser.add_argument('-noSort', action='store_true', default=False,
    #                     dest='noSort',
    #                     help='set this optional parameter if the constrains shouldn\'t be sorted inside of clusters')
    # parser.add_argument('-colorTheme', action='store', type=str, default="plasma", dest='colorTheme',
    #                     help='set the option for the colors of the Drift Map, the option can be found '
    #                          'https://matplotlib.org/users/colormaps.html, we recommend \'plasma\' or \'PiYG\' or \'bw\'')
    # parser.add_argument("-typeConstr", default='confidence', help="\'support\', \'confidence\' or \'interestFactor\'")
    # Initialization of the default parameters for the command line arguments
    # args = parser.parse_args()



    linkage_method = 'ward'
    linkage_metric = 'euclidean'
    fcluster_metric = 'distance' # other option is = 'maxclust'

    algoPrmts = AlgorithmParameters(subL,
                                   sliBy,
                                   cluCut,
                                   fcluster_metric,
                                   linkage_method,
                                   linkage_metric,
                                   driftAll,
                                   noSort,
                                   colorTheme,
                                   typeConstr)
    fileMngm = FilesManagement(logName,algoPrmts)

    return fileMngm, algoPrmts
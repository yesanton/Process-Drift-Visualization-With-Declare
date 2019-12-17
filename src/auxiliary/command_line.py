'''
This script is used when the app will be used with the command line arguments
to parce and understand them
Example run:
python3 draw_graph.py -logName bpi_challenge_2013_open -logFolder bpic2013 -subL 100 -sliBy 50 -caseID 0 -timestampID 3 -noMinerful -driftAll

call help to see argument list
Author:  Anton Yeshchenko
'''

# lib documentation
# https://pymotw.com/2/argparse/
import argparse

def get_commandline_parameters():


    parser = argparse.ArgumentParser()

    # These are the argument list  of theimport subprocess script
    parser.add_argument("-logName", help="the log name")
    #parser.add_argument("-logFolderName", help="the folder with a timestamp sorted log, check https://github.com/yesanton/Event-Log-Preprocessing-Tools for timeseoring of CSVs")
    #parser.add_argument("-caseID", type=int)
    #parser.add_argument("-timestampID", type=int)
    #TODO sort optionally (no sort by timestamp is optionaL)
    parser.add_argument("-subL", type=int)
    parser.add_argument("-sliBy", type=int)
    parser.add_argument("-cluCut", type=int, help="Cutoff threshold for cluster algorithm")
    parser.add_argument('-driftAll', action='store_true', default=False,
                        dest='driftAll',
                        help='set this optional parameter if you want to generale change points for the whole set at the same time (if not set, every cluster will get its own changepoint)')

    parser.add_argument('-noSort', action='store_true', default=False,
                        dest='noSort',
                        help='set this optional parameter if the constrains shouldn\'t be sorted inside of clusters')

    parser.add_argument('-colorTheme', action='store', type=str, default="plasma", dest='colorTheme',
                        help='set the option for the colors of the Drift Map, the option can be found https://matplotlib.org/users/colormaps.html, we recommend \'plasma\' or \'PiYG\' or \'bw\'')

    #parser.add_argument("-type", type=int, help='0 support, 1 confidence, 2 interstFactor')
    # parser.add_argument("-colors", help="[bw] for black and while, [yb] for yellow to blue")


    # Initialization of the default parameters for the command line arguments
    args = parser.parse_args()
    tStart = 0
    if args.subL:
        subL = args.subL
    else:
        subL = 100

    if args.sliBy:
        sliBy = args.sliBy
    else:
        sliBy = 50
    # if args.type:
    #     iii = args.type
    # else:
    #     iii = 0 # 0 support, 1 confidence, 2 interstFactor

    # if args.colors:
    #     colors = args.colors
    # else:
    #     colors = 'bw'

    if args.logName:
        dataset_name = args.logName
    else:
        dataset_name = ''




    # if args.caseID:
    #     caseID = args.caseID
    # else:
    #     caseID = 0
    #
    # if args.timestampID:
    #     timestampID = args.timestampID
    # else:
    #     timestampID = 0

    # clustering parameters
    if not args.cluCut:
        fcluster_value = 300
    else:
        fcluster_value = args.cluCut

    linkage_method = 'ward'
    linkage_metric = 'euclidean'
    fcluster_metric = 'distance'
    # fcluster_metric = 'maxclust'

    colorTheme = args.colorTheme

    return dataset_name, tStart, subL, sliBy, fcluster_value, fcluster_metric, linkage_method, linkage_metric, args.driftAll, args.noSort, colorTheme
'''
this file we define the autocorrelation plots executuion
'''
from src.auxiliary.command_line import get_commandline_parameters
from src.visualize_autocorrelation_plots import visualize_autocorrelation_plots

fileMngm, algoPrmts = get_commandline_parameters()

visualize_autocorrelation_plots(fileMngm)


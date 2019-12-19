from src.auxiliary.command_line import get_commandline_parameters
from src.visualize_dfg_with_constraints import visualize_dfg_with_constraints

fileMngm, algoPrmts = get_commandline_parameters()

visualize_dfg_with_constraints(fileMngm)


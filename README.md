# Comprehensive Process Drift Detection with Visual Analytics (VDD technique)

This technique supports the discovery of process drifts in the processes from event logs in several different visual representations:
- Drift map - get an overview of all logs in your dataset
- Drift plot - get a precise trend of one specific drift (a real-life process usually has several parallel drifts, so our visualizations will show you how exactly your process drifts)
- DFG visualization - for each specific drift (shown in Drift plot and Drift map) we display what exactly is affected. We do that in the easy to understand visualizations that is a combination of 
Directly Follows Graphs and annotations from Declare constraint)
 
Our library supports standard process mining logs (xes format).

### Watch a [youtube video explaining this method here](https://youtu.be/_AZpI_YTjO8)

### Visualization system is available [at the address](https://yesanton.github.io/driftvis)

## How to run

In order to run the tool, one runs the script that composes the version of the app you need. The example is to run the 
first scenario with following command in the terminal:

> python3 scenario_1.py italian_help_desk  -subL 100 -sliBy 50

Where essential parameters (such as subL - the size of the window for mining constraints (refer to our published papers in the folder XXX for theoretical details), and sliBy for a sliding window size)

To discover the parameters useful for the analysis, run the previous command with a \'-help\' parameter

Here is one way to run the tool

the '-logName' refers to the .xes found in the folder \'data_initial/ \'

\'-subL\' the sublog size

\'sliBy\' slide by argument

\'-driftAll\' this indicates that for discovering the points where the drifts are most redically changing, we use information from all subs-drifts at the same time.

## Fastest way to get up to speed (if you have all required libraries)

### Run all these in terminal in a folder in your computer, and right away you have your analysis.

> git clone git@github.com:yesanton/Process-Drift-Visualization-With-Declare.git

> cd Process-Drift-Visualization-With-Declare

> python3 scenario_1.py italian_help_desk  -subL 100 -sliBy 50



## Requirements for running software

- Python 3 
- [pm4py](https://github.com/pm4py) library for python 
- Requires java 10 (for the MINERful module (included in this software distribution), also find the original repo of MINERful – [fork MINERful](https://github.com/cdc08x/MINERful/wiki))
- Command line
- You can use disco, prom or any other tool for conversion between .csv and .xes files

## Datasets

Code support any standard event log with that features case ID, timestamps, and activity labels.

## Why

This is the source code and tool supporting the conference paper:
Anton Yeshchenko, Claudio Di Ciccio, Jan Mendling, Artem Polyvyanyy: *Comprehensive Process Drift Detection with Visual Analytics*. In: Proc. of [ER](http://www.inf.ufrgs.br/er2019/) (in print). 2019. [Open arXiv pre-print](https://arxiv.org/abs/1907.06386). And [here at Springer](https://link.springer.com/chapter/10.1007/978-3-030-33223-5_11)



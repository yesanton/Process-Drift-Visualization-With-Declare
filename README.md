# Comprehensive Process Drift Detection with Visual Analytics (VDD technique)

This technique supports the discovery of process drifts in the processes from event logs. 
Load your [timestamp sorted csv](https://github.com/yesanton/Event-Log-Preprocessing-Tools) and xes files to the tool to discover Drfit Maps, Drift charts, and 
Declare relations that see which part of the log is changing.

## How to run

In order to run the tool, one runs the following command in the terminal:

> python3 draw_graph.py 

To discover the parameters useful for the analysis, run the previous command with a \'-help\' parameter

Here is one way to run the tool

> python3 draw_graph.py -logName italian_help_desk -logFolder  italian_help_desk  -subL 100 -sliBy 50 -caseID 0 -timestampID 2  -driftAll

\'-logFolder\' is an the subfolder dedicated to the log inside of \'data_initial/\'folder in the project folder 

the '-logName' refers to the .xes and .csv files name found in the folder \'data_initial/logFolder \'

\'-subL\' the sublog size

\'sliBy\' slide by argument

\'-caseID\' the case id (the column with case id in the csv file)

\'-timestampID\' the timestamp id (the column with timestamps in the csv file)

\'-driftAll\' this indicates that for discovering the points where the drifts are most redically changing, we use information from all subs-drifts at the same time.

## Fastest way to get up to speed (if you have all required libraries)

### Run all these in terminal in a folder in your computer, and right away you have your analysis.

> git clone git@github.com:yesanton/Process-Drift-Visualization-With-Declare.git
> cd Process-Drift-Visualization-With-Declare
> python3 draw_graph.py -logName italian_help_desk -logFolderName italian_help_desk -caseID 0 -timestampID 3 -subL 400 -sliBy 200
> cd graphs_produced



## Requirements for running software

- Python 3 
- Requires java 10 (for the MINERful module (included in this software distribution), also find the original repo of MINERful – [fork MINERful](https://github.com/cdc08x/MINERful/wiki))
- Command line
- You can use disco, prom or any other tool for conversion between .csv and .xes files

## Datasets

Code support any standard event log with that features case ID, timestamps, and activity labels.

## Why


This is the source code and tool supporting the conference paper:
Anton Yeshchenko, Claudio Di Ciccio, Jan Mendling, Artem Polyvyanyy: *Comprehensive Process Drift Detection with Visual Analytics*. In: Proc. of [ER](http://www.inf.ufrgs.br/er2019/) (in print). 2019. [Open the pre-print](https://github.com/yesanton/Process-Drift-Visualization-With-Declare/blob/master/Yeshchenko-etal-ER2019.pdf).

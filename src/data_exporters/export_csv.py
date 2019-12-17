import csv

def export_one_line_csvs(timestamps, file_name):
    with open(file_name, 'w', newline='') as myfile:
        wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
        wr.writerow(timestamps)




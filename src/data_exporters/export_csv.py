import csv

def export_one_line_csvs(timestamps, file_name):
    with open(file_name, 'w', newline='') as myfile:
        wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
        wr.writerow(timestamps)

def export_many_line_csvs(list, filename):
    writeFile = open(filename, 'w')
    writerFile = csv.writer(writeFile)
    for li in list:
        writerFile.writerow(li)

    writeFile.close()
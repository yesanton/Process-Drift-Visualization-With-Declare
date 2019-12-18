import csv
from pathlib import Path

cluster = "italian_help_deskplot_confidence_0_100_50_ward_euclidean_300_distance_changepoints_separatelycl-"
out_file = "cluster-timeseries-"

def transform_files(cluster,out_file):

    event_log = Path("from_minerful/italian_help_desk_0_100_50.csv")

    with open(cluster) as one_cluster_example:
        reader = csv.reader(one_cluster_example, delimiter=';', quotechar='|', quoting=csv.QUOTE_MINIMAL)
        next(reader, None)

        constr_cluster = set()
        for row in reader:
            # print(row)
            constr_cluster.add(row[0].replace(" ", ""))

    print(constr_cluster)


    find_columns_with_constraints = []


    f_out = open(out_file, 'w',newline='')
    writer = csv.writer(f_out, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

    with open(event_log) as event_l:
        reader = csv.reader(event_l, delimiter=';', quotechar='|', quoting=csv.QUOTE_MINIMAL)
        header = next(reader, None)
        header2 = next(reader, None)
        print(header)

        header_out = []

        for i in range(len(header)):
            if header[i].replace(" ", "") in constr_cluster:
                print(header[i] + ' ' + header2[i+1])
                find_columns_with_constraints.append(i+1)
                header_out.append(header[i])
        writer.writerow(header_out)


        for row in reader:
            new_line = []
            for ind in find_columns_with_constraints:
                new_line.append(row[ind])
            writer.writerow(new_line)

        # for row in reader:
        #     print(row)

    f_out.close()
    print(find_columns_with_constraints)

for i in range(17):
    transform_files(Path(cluster + str(i) + '.csv'), Path(out_file + str(i) + '.csv'))
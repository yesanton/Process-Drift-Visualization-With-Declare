import math


def save_separately_timestamp_for_each_constraint_window(
        sliding_window_step,
        window_size,
        log):

    # every first timestamp of each trace is stored here
    timestamps = [trace._list[0]._dict['time:timestamp'].strftime('%m-%d-%Y') for trace in log._list]

    # csvfile = open(Path('./timestamps.csv'), 'w')
    # results_writer = csv.writer(csvfile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)

    time_out = []
    n_th = 0
    number_of_timestamps = (len(timestamps) - window_size) / sliding_window_step
    skip_every_n_th = math.ceil(number_of_timestamps / 30)

    # timestamps = sorted(timestamps)
    for i in range(0, len(timestamps) - window_size, sliding_window_step):
        # print (timestamps[i] + " for from: " + str(i) + ' to ' + str(i+window_size))
        # results_writer.writerow([timestamps[i]])
        if n_th % skip_every_n_th == 0:
            time_out.append(timestamps[i])
        else:
            time_out.append(" ")
        n_th += 1
    return time_out
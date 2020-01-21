import math

def save_separately_timestamp_for_each_constraint_window(log, algoPrmts):
    # every first timestamp of each trace is stored here
    try:
        timestamps = [trace._list[0]._dict['time:timestamp'].strftime('%m-%d-%Y') for trace in log._list]
    except AttributeError:
        timestamps = [trace._list[0]._dict['time:timestamp'][0:8] for trace in log._list]
    time_out = []
    n_th = 0
    number_of_timestamps = (len(timestamps) - algoPrmts.window_size) / algoPrmts.sliding_window_size
    skip_every_n_th = math.ceil(number_of_timestamps / 30)

    # timestamps = sorted(timestamps)
    for i in range(0, len(timestamps) - algoPrmts.window_size, algoPrmts.sliding_window_size):
        # print (timestamps[i] + " for from: " + str(i) + ' to ' + str(i+window_size))
        # results_writer.writerow([timestamps[i]])
        if n_th % skip_every_n_th == 0:
            time_out.append(timestamps[i])
        else:
            time_out.append(" ")
        n_th += 1
    return time_out
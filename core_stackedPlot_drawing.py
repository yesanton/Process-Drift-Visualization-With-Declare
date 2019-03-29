# library
import matplotlib.pyplot as plt
import numpy


def drawStackedAll(ts = None, clusters_dict=None, cluster_order = None):
    lines_for_lineplot = []
    for key in cluster_order:
        averaged_line = [0] * (len(clusters_dict[key][0]) - 3)
        for i in range(len(clusters_dict[key])):
            for j in range(len(averaged_line)):
                averaged_line[j] += clusters_dict[key][i][j + 3]

        # for j in range(len(averaged_line)):
        #     averaged_line[j] /= len(clusters_dict[key])

        lines_for_lineplot.append(averaged_line)

    # Data
    x = range(0, len(lines_for_lineplot[0]))
    plt.clf()
    # Plot
    plt.stackplot(x, lines_for_lineplot)  # , labels=['A', 'B', 'C']
    plt.xticks(x, ts, rotation='vertical')
    plt.legend(loc='upper left')
    plt.show()


def drawStackedOne(ts = None, clusters_dict=None, key = None):
    averaged_line = [0] * (len(clusters_dict[key][0]) - 3)
    for i in range(len(clusters_dict[key])):
        for j in range(len(averaged_line)):
            averaged_line[j] += clusters_dict[key][i][j + 3]

    for j in range(len(averaged_line)):
        averaged_line[j] /= len(clusters_dict[key])

    from scipy.interpolate import make_interp_spline, BSpline

    xnew = range(0, len(averaged_line))
    # xnew = numpy.linspace(0, len(averaged_line), 300)  # 300 represents number of points to make between T.min and T.max
    spl = make_interp_spline(range(len(averaged_line)), averaged_line, k=2)  # BSpline object
    power_smooth = spl(xnew)

    # Data

    plt.clf()
    # Plot
    plt.stackplot(xnew, power_smooth)  # , labels=['A', 'B', 'C']

    ynew = [(power_smooth[0]+power_smooth[1] + power_smooth[2])/3] + \
           [(power_smooth[0] + power_smooth[1] + power_smooth[2] + power_smooth[3]) / 4] + \
           [(i+j+k+l+g)/5 for i, j, k, l, g in zip(power_smooth[:-4],power_smooth[1:-3],power_smooth[2:-2], power_smooth[3:-1], power_smooth[4:])] + \
           [(power_smooth[-4] + power_smooth[-3] + power_smooth[-2] + power_smooth[-1])/4] + \
           [(power_smooth[-3] + power_smooth[-2] + power_smooth[-1]) / 3]

    plt.plot(xnew,ynew)
    plt.xticks(xnew, ts,rotation='vertical')
    plt.legend(loc='upper left')
    plt.show()

    dis_should_be = 0
    dis_is_with_a_drift = 9

    y_0 = ynew[0]
    for y in ynew[1:]:
        dis_should_be += xnew[1] - xnew[0]
        dis_is_with_a_drift += numpy.math.sqrt((xnew[1] - xnew[0]) ** 2 + (y - y_0)**2)
        y_0 = y

    print ("without DRIFT: " + str(dis_should_be))
    print("current DRIFT: " + str(dis_is_with_a_drift))


    # plt.clf()
    # from scipy.interpolate import make_interp_spline, BSpline
    # xnew = numpy.linspace(0, len(averaged_line), 200)  # 300 represents number of points to make between T.min and T.max
    # spl = make_interp_spline(range(len(averaged_line)), averaged_line, k=1)  # BSpline object
    # power_smooth = spl(xnew)
    # plt.plot(xnew, power_smooth)
    # plt.show()

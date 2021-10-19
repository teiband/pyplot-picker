import matplotlib.pyplot as plt
import numpy as np
from matplotlib.lines import Line2D
from matplotlib.patches import Rectangle

points = []
points_ind = []


def get_picked_segment(x_start_idx, x_end_idx, x_all, y_all):
    if x_start_idx > x_end_idx:
        x_start_idx, x_end_idx = x_end_idx, x_start_idx
    x_seg = x_all[x_start_idx: x_end_idx]
    y_seg = y_all[x_start_idx: x_end_idx]
    return x_seg, y_seg


if True:
    fig, ax = plt.subplots()
    ax.set_title('click on points', picker=True)
    ax.set_ylabel('ylabel', picker=True)

    t_graph = np.arange(0, 10, 0.1)
    y_graph = np.sin(t_graph)
    graph_obj = ax.plot(t_graph, y_graph, 'o', picker=5)

    lines = []


    def onpick1(event):
        if isinstance(event.artist, Line2D):
            thisline = event.artist
            xdata = thisline.get_xdata()
            ydata = thisline.get_ydata()
            ind = event.ind
            x_ind = ind[0]
            x = np.take(xdata, ind)[0]
            y = np.take(ydata, ind)[0]
            print('X=' + str(x))  # Print X point
            print('Y=' + str(y))  # Print Y point
            points.append((x, y,))
            points_ind.append(x_ind)

            line = ax.vlines(x, -1, 1)
            lines.append(line)
            plt.draw()

            if len(points_ind) == 2:
                x_seg, y_seg = get_picked_segment(points_ind[0], points_ind[1], t_graph, y_graph)

                ax.plot(x_seg, y_seg, 'r')
                plt.draw()
                print("2 points selected")
                print(ax.lines)
                print(lines)
                lines[0].remove()
                lines[1].remove()
                Rectangle(points[0], points[1][0] - points[0][0], points[1][1] - points[0][1])
                lines.clear()
                points_ind.clear()
                plt.draw()


    fig.canvas.mpl_connect('pick_event', onpick1)
    plt.show()

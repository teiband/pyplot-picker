import matplotlib.pyplot as plt
from matplotlib.lines import Line2D
from matplotlib.patches import Rectangle
from matplotlib.text import Text
from matplotlib.image import AxesImage
import numpy as np
import time

points = []

if True:
    fig, ax = plt.subplots()
    ax.set_title('click on points', picker=True)
    ax.set_ylabel('ylabel', picker=True)

    t = np.arange(0,10,0.1)
    y = np.sin(t)
    ax.plot(t, y, 'o', picker=5)

    lines = []

    def onpick1(event):
        if isinstance(event.artist, Line2D):
            thisline = event.artist
            xdata = thisline.get_xdata()
            ydata = thisline.get_ydata()
            ind = event.ind
            x = np.take(xdata, ind)[0]
            y = np.take(ydata, ind)[0]
            print('X='+str(x)) # Print X point
            print('Y='+str(y)) # Print Y point
            points.append((x, y,))

            line = ax.vlines(x, -1, 1)
            lines.append(line)
            plt.draw()

            if len(points) == 2:
                t_seg = np.arange(points[0][0], points[1][0])
                #ax.plot([1,2,3], [1,2,3], 'o', picker=5)
                print("2 points selected")
                print(ax.lines)
                print(lines)
                lines[0].remove()
                lines[1].remove()
                Rectangle(points[0], points[1][0]-points[0][0], points[1][1]-points[0][1])
                lines.clear()
                points.clear()
                plt.draw()


    fig.canvas.mpl_connect('pick_event', onpick1)
    plt.show()
import sunpy.map
import matplotlib.pyplot as plt
from skimage import exposure, img_as_float

def plot_map_histogram(vmin=None, vmax=None):
    aia = sunpy.map.Map(AIA171)
    if not vmin:
        vmin = aia.data.min()
    if not vmax:
        vmax = aia.data.max()
    plt.figure(figsize=(15,5))
    ax1 = plt.subplot(1, 2, 1)
    aia.plot(vmin=vmin, vmax=vmax)
    plt.colorbar()

    ax2 = plt.subplot(1, 2, 2)
    y,x = exposure.histogram(aia.data, nbins=100)
    ax2.plot(x, y)
    ax2.set_xrange=[aia.min() - 1000, aia.max() + 1000]
    ax2.axvline(vmin, color='r')
    ax2.axvline(vmax, color='g')


if __name__ == '__main__':
    plot_map_histogram()
    plot_map_histogram(vmin=0, vmax=100)
    plot_map_histogram(vmin=500, vmax=5000)
    plt.show()

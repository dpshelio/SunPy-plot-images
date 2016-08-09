import sunpy
import sunpy.map
import matplotlib.pyplot as plt

aia = sunpy.map.Map('/home/sudarshan/AIA20110319_105400_0171.fits')
aia.plot(vmin=100, vmax=4000)
plt.colorbar()
plt.draw()
##raw_input()

plt.figure()
plt.hist(aia.data, bins=100)
plt.draw()

plt.show()

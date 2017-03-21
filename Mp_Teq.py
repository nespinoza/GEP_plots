import numpy as np
import matplotlib.pyplot as plt
plt.style.use('ggplot')
import Utils

Utils.downloadPlanetList()
out = Utils.getPlanetData()

idx = np.where((out['mplanet']>0.)&(out['teqplanet']>0.))[0]
plt.plot(out['mplanet'][idx],out['teqplanet'][idx],'.')
plt.xlabel(r'Planet mass ($M_J$)')
plt.ylabel(r'Planet equilibrium temperature')
plt.show()

import os
import numpy as np

# Download latest exoplanet list:
def downloadPlanetList(update=False):
    if not os.path.exists('allplanets-ascii.txt') or update:
        os.system('wget http://www.astro.keele.ac.uk/jkt/tepcat/allplanets-ascii.txt')

def getPlanetData():
    f = open('allplanets-ascii.txt','r')
    out = {}
    out['name'] = np.array([])
    out['mplanet'] = np.array([])
    out['rplanet'] = np.array([])
    out['gplanet'] = np.array([])
    out['teqplanet'] = np.array([])
    out['porb'] = np.array([])
    out['rstar'] = np.array([])
    while True:
        line = f.readline()
        if line == '':
            break
        elif line[0] != '#':
            splitted_line = line.split()
            name,mplanet,rplanet,gplanet,Teqplanet,Porb,rstar = splitted_line[0],splitted_line[26],splitted_line[29],\
                                                                splitted_line[32],splitted_line[38],splitted_line[19],\
                                                                splitted_line[10]

            out['name'] = np.append(out['name'],name)
            out['mplanet'] = np.append(out['mplanet'],np.float(mplanet))
            out['rplanet'] = np.append(out['rplanet'],np.float(rplanet))
            out['gplanet'] = np.append(out['gplanet'],np.float(gplanet))
            out['teqplanet'] = np.append(out['teqplanet'],np.float(Teqplanet))
            out['porb'] = np.append(out['porb'],np.float(Porb))
            out['rstar'] = np.append(out['rstar'],np.float(rstar))
    f.close()
    return out

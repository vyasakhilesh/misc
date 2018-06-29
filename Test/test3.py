import numpy as np
import scipy.misc as msc
import scipy.ndimage as img
def foreground2BinImg(f):
    d = img.filters.gaussian_filter(f, sigma=0.50, mode='reflect') - img.filters.gaussian_filter(f, sigma=1.00, mode='reflect')
    d = np.abs(d)
    m = d.max()
    d[d< 0.1*m] = 0
    d[d>=0.1*m] = 1
    return img.morphology.binary_closing(d)
imgName = 'lightning-3'
f = msc.imread(imgName+'.png', flatten=True).astype(np.float)
g = foreground2BinImg(f)
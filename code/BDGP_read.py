from os import listdir
from os.path import isfile, join
import glob

from PIL import Image

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm


image = Image.open('../data/BDGP/insitu10000_s.bmp').convert("L")
arr = np.asarray(image)
plt.imshow(arr, cmap = cm.Greys_r)
plt.show()

# lab = open('label.txt', 'r')
# d = {}
# for line in lab:
# 	[s, t] = line.split(' ')
# 	d[s] = int(t)

imgs = listdir('../data/BDGP')

print imgs


# open random image of dimensions 639x516
#img = asarray(img, dtype='float64') / 256.

#print img



	





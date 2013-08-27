from os import listdir
from os.path import isfile, join
import glob

from PIL import Image

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm

import gzip
import cPickle



n = 32 * 80
# image = Image.open('../data/BDGP/insitu10000_s.bmp').convert("L")
# arr = np.asarray(image)
# plt.imshow(arr, cmap = cm.Greys_r)
# plt.show()

train_size = 2400
train_file = open('../data/BDGP_reshape/trData.txt', 'r')
train_data = np.zeros([2400, n])
a = [0] * train_size 
line_cnt = 0
for line in train_file:
	[name, lab] = line.split(' ')
	train_data[line_cnt,] = np.reshape(np.asarray(Image.open('../data/BDGP_reshape/' + name), dtype='float32'), n)
	a[line_cnt] = int(lab)
	line_cnt += 1
	
train_set = [train_data, np.asarray(a)]

test_size = 721
test_file = open('../data/BDGP_reshape/tstData.txt', 'r')
test_data = np.zeros([test_size, n])
a = [0] * test_size
line_cnt = 0
for line in test_file:
	[name, lab] = line.split(' ')
	test_data[line_cnt,] = np.reshape(np.asarray(Image.open('../data/BDGP_reshape/' + name), dtype='float32'), n)
	a[line_cnt] = int(lab)
	line_cnt += 1
	
test_set = [test_data, np.asarray(a)]

valid_size = 600
valid_file = open('../data/BDGP_reshape/valData.txt', 'r')
valid_data = np.zeros([valid_size, n])
a = [0] * valid_size
line_cnt = 0
for line in valid_file:
	[name, lab] = line.split(' ')
	valid_data[line_cnt,] = np.reshape(np.asarray(Image.open('../data/BDGP_reshape/' + name), dtype='float32'), n)
	a[line_cnt] = int(lab)
	line_cnt += 1
 	
valid_set = [valid_data, np.asarray(a)]


cPickle.dump([train_set, valid_set, test_set], open('../data/bdgp_reshape.pkl', 'wb'), protocol=-1)

f_in = open('../data/bdgp_reshape.pkl', 'rb')
f_out = gzip.open('../data/bdgp_reshape.pkl.gz', 'wb')
f_out.writelines(f_in)
f_out.close()
f_in.close()




# d = {}
# for line in lab:
# 	[s, t] = line.split(' ')
# 	d[s] = int(t)

#imgs = listdir('../data/BDGP')

#print imgs


# open random image of dimensions 639x516
#img = asarray(img, dtype='float64') / 256.

#print img



	








import glob
import os
print(glob.glob('./samples/*'))


path = './samples/'
files = glob.glob(path+'*')

for i, f in enumerate(files):
    fname = './{num:06d}.jpg'.format(num = i)
    os.rename(f, path + fname)

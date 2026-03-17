"""
Python files to read dummy dataset created by data_create.py
"""

import os
import tarfile
import numpy as np
import matplotlib.pyplot as plt
import paths

# open tarfile
tar_path=paths.data / 'data.tar.gz'
tar=tarfile.open(tar_path, 'r:gz')

# read trail
exp_idx=0

while True:
    try:
        txt_file_path = tar.extractfile(f'data/exp_{exp_idx}/data.txt')
        data = np.loadtxt(txt_file_path, comments='#', dtype=float)
        x=data[:,0]
        y=data[:,1]
        x_noise=data[:,2]
        y_noise=data[:,3]
        # x_red, y_red=data_angle_cor(x_noise, y_noise, alpha_val)
        plt.plot(x_noise,y_noise,'o')
        exp_idx += 1
    except KeyError:
        break

plt.savefig(paths.figures / 'raw_data.pdf')
print('The end')
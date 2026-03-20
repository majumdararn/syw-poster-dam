"""
Plot script for plotting reduced raw data
raw doi: 10.5281/zenodo.19115565
cache doi: 10.5281/zenodo.19115970
"""

import tarfile
import numpy as np
import matplotlib.pyplot as plt
import paths

# open reduced data as tarfile
tar_path=paths.data / 'red_data.tar.gz'
tar=tarfile.open(tar_path, 'r:gz')

# initialize figure
plt.figure(figsize=(8, 4))

# read data
exp_idx=0
while True:
    try:
        # reduced data file read for each measurement
        txt_file_name = f'red_data/red_exp_{exp_idx}/red_data.txt'
        txt_file_path = tar.extractfile(txt_file_name)
        data = np.loadtxt(txt_file_path, comments='#', dtype=float)
        x_red=data[:,0]
        y_red=data[:,1]
        # plot
        label_name=f'Measurement {exp_idx}'
        plt.plot(x_red,y_red,'o', label=label_name)
        exp_idx += 1
    except KeyError:
        break
# plot formatting and saving
plt.xlabel('Pixel positions [A.U.]', fontsize=15)
plt.ylabel('Measurement amplitude [A.U.]', fontsize=15)
plt.xticks(fontsize=20)
plt.yticks(fontsize=20)
plt.legend(fontsize=15, ncols=1, loc='center left', bbox_to_anchor=(1, 0.5))
plt.tight_layout()
plt.savefig(paths.figures / 'red_data.pdf')

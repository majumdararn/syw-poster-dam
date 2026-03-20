"""
Plot script for plotting raw data
Raw data doi: 10.5281/zenodo.19115970
"""

import os
import tarfile
import numpy as np
import matplotlib.pyplot as plt
import paths

# open raw data tarfile
tar_path=paths.data / 'data.tar.gz'
tar=tarfile.open(tar_path, 'r:gz')

# read raw data for all measurements (in this case 10)
exp_idx=0
# initialize plot figure
plt.figure(figsize=(8, 4))
# loop until measurement data exist
while True:
    try:
        # text file containing measured  data
        txt_file_path = tar.extractfile(f'data/exp_{exp_idx}/data.txt')
        data = np.loadtxt(txt_file_path, comments='#', dtype=float)
        # data read
        raw_x=data[:,2]
        raw_y=data[:,3]
        # plotting raw data
        label_name=f'Measurement {exp_idx}'
        plt.plot(raw_x,raw_y,'o', label=label_name)
        exp_idx += 1
    except KeyError:
        break
# plot formatting 
plt.xlabel('Pixel positions [A.U.]', fontsize=15)
plt.ylabel('Measurement amplitude [A.U.]', fontsize=15)
plt.xticks(fontsize=15)
plt.yticks(fontsize=15)
plt.legend(fontsize=15, ncols=1, loc='center left', bbox_to_anchor=(1, 0.5))
plt.tight_layout()
plt.savefig(paths.figures / 'raw_data.pdf')

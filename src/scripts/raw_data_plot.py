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
# while os.path.exists(tar.extractfile(f'data/exp_{exp_idx}')):
#     txt_file_path=tar.extractfile(f'data/exp_{exp_idx}/data.txt')
#     data=np.loadtxt(txt_file_path, comments='#', dtype='float')
#     x=data[:,0]
#     y=data[:,1]
#     x_noise=data[:,2]
#     y_noise=data[:,3]
#     # x_red, y_red=data_angle_cor(x_noise, y_noise, alpha_val)
#     plt.plot(x_noise,y_noise,'o')
    # plt.show()
    # final_data_dir=f'exp_{exp_idx}_red'
    # final_data_dir=os.path.join(final_dir, final_data_dir)
    # os.makedirs(final_data_dir, exist_ok=True)
    # final_txt_file='data_red.txt'
    # final_txt_file_loc=os.path.join(final_data_dir, final_txt_file)
    # data_red = np.column_stack((x_red, y_red))
    # np.savetxt(final_txt_file_loc,
    #             data_red, header='x_red x_red', fmt="%.6f")
    # exp_idx+=1
plt.savefig(paths.figures / 'raw_data.pdf')
print('The end')
# make a tar file
# Create a compressed tar.gz archive
# with tarfile.open('data_red.tar.gz', 'w:gz') as tar:
#     tar.add('data_red', arcname=os.path.basename('data_red'))
# print('Info>> Saved reduced data as tar file')
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
data=tarfile.open(tar_path, 'r:gz')

# # cwd
# print('Getting current working dir (cwd):')
# cwd=os.getcwd()
# print('cwd: ', cwd)

# # create dir for savinf reduced data
# final_dir='data_red'
# os.makedirs(final_dir, exist_ok=True)

# # open tarfile
# tar=tarfile.open('data.tar.gz', 'r:gz')
# data=tar.extractfile('data')

# read trail
exp_idx=0
while os.path.exists(f'data/exp_{exp_idx}'):
    # print(f'exists exp data/exp_{exp_idx}')
    # print(f'reading data.txt from data/exp_{exp_idx}')
    txt_file_path=f'data/exp_{exp_idx}/data.txt'
    # with open(txt_file_path, "r") as f:
    #     # Read the first two lines
    #     _ = f.readline()  # first line (skip)
    #     second_line = f.readline()  # second line
    #     alpha_val_str=second_line[9:]
    #     alpha_val=float(alpha_val_str)
    #     print(f'Rotation angle is: {alpha_val}')
    data=np.loadtxt(txt_file_path, comments='#', dtype='float')
    x=data[:,0]
    y=data[:,1]
    x_noise=data[:,2]
    y_noise=data[:,3]
    # x_red, y_red=data_angle_cor(x_noise, y_noise, alpha_val)
    plt.plot(x_noise,y_noise,'o')
    # plt.show()
    # final_data_dir=f'exp_{exp_idx}_red'
    # final_data_dir=os.path.join(final_dir, final_data_dir)
    # os.makedirs(final_data_dir, exist_ok=True)
    # final_txt_file='data_red.txt'
    # final_txt_file_loc=os.path.join(final_data_dir, final_txt_file)
    # data_red = np.column_stack((x_red, y_red))
    # np.savetxt(final_txt_file_loc,
    #             data_red, header='x_red x_red', fmt="%.6f")
    exp_idx+=1
plt.savefig(paths.figures / 'raw_data.pdf')
print('The end')
# make a tar file
# Create a compressed tar.gz archive
# with tarfile.open('data_red.tar.gz', 'w:gz') as tar:
#     tar.add('data_red', arcname=os.path.basename('data_red'))
# print('Info>> Saved reduced data as tar file')
"""
Python files to read dummy dataset created by data_create.py
"""

import os
import tarfile
import numpy as np
import matplotlib.pyplot as plt
import paths

# # functions
# def data_angle_cor(x_raw, y_raw, angle):
#     """
#     correct rotation of data
#     x_raw = raw x data
#     y_raw = raw y data
#     angle = anglre to be corrected
#     """
#     # angle for undo rotation
#     angle_opp=-angle

#     # coefficients for undo rotation
#     cos_a = np.cos(angle_opp)
#     sin_a = np.sin(angle_opp)

#     # undo rotation
#     x_angle_cor = x_raw * cos_a - y_raw * sin_a
#     y_angle_cor = x_raw * sin_a + y_raw * cos_a

#     return x_angle_cor, y_angle_cor

# create dir for savinf reduced data
final_dir='data_red'
os.makedirs(final_dir, exist_ok=True)

# open tarfile
tar_path=paths.data / 'data.tar.gz'
tar=tarfile.open(tar_path, 'r:gz')
print("I am here")

# read trail
exp_idx=0

for name in tar.getnames():
    print(name)

while True:
    try:
        txt_file_name = f'data/exp_{exp_idx}/data.txt'
        txt_file_path = tar.extractfile(txt_file_name)
        # txt_file_name=f'data/exp_{exp_idx}/data.txt'
        data = np.loadtxt(txt_file_path, comments='#', dtype=float)
        txt_file_path = tar.extractfile(txt_file_name)
        with txt_file_path as f:
            # read header
            _ = f.readline()                      # "# Experimental condition:"
            second_line = f.readline().decode()   # "# alpha = ..."
            _ = f.readline()                      # "# x y noisy_x noisy_y"
            print(repr(second_line))
            # extract alpha
            alpha_val = (second_line.split("=")[1])
            print(f"Rotation angle is: {alpha_val}")
            # # Read the first two lines
            # _ = f.readline()  # first line (skip)
            # # print()
            # second_line = f.readline().decode().strip()  # second line
            # print(second_line)
        #     alpha_val_str=second_line[9:]
        #     alpha_val=float(alpha_val_str)
        #     print(f'Rotation angle is: {alpha_val}')
        x_red=data[:,0]
        y_red=data[:,1]
        # x_red, y_red=data_angle_cor(x_noise, y_noise, alpha_val)
        plt.plot(x_red,y_red,'o')
        exp_idx += 1
    except KeyError:
        break
plt.savefig(paths.figures / 'red_data.pdf')
print('The end')

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

# # read trail
# exp_idx=0
# while os.path.exists(f'data/exp_{exp_idx}') and exp_idx<5:
#     print(f'exists exp data/exp_{exp_idx}')
#     print(f'reading data.txt from data/exp_{exp_idx}')
#     txt_file_path=f'data/exp_{exp_idx}/data.txt'
#     with open(txt_file_path, "r") as f:
#         # Read the first two lines
#         _ = f.readline()  # first line (skip)
#         second_line = f.readline()  # second line
#         alpha_val_str=second_line[9:]
#         alpha_val=float(alpha_val_str)
#         print(f'Rotation angle is: {alpha_val}')
#     data=np.loadtxt(txt_file_path, comments='#', dtype='float')
#     x=data[:,0]
#     y=data[:,1]
#     x_noise=data[:,2]
#     y_noise=data[:,3]
#     x_red, y_red=data_angle_cor(x_noise, y_noise, alpha_val)
#     plt.plot(x_red,y_red,'o')
#     plt.show()
#     final_data_dir=f'exp_{exp_idx}_red'
#     final_data_dir=os.path.join(final_dir, final_data_dir)
#     os.makedirs(final_data_dir, exist_ok=True)
#     final_txt_file='data_red.txt'
#     final_txt_file_loc=os.path.join(final_data_dir, final_txt_file)
#     data_red = np.column_stack((x_red, y_red))
#     np.savetxt(final_txt_file_loc,
#                 data_red, header='x_red x_red', fmt="%.6f")
#     exp_idx+=1
# print('The end')
# # make a tar file
# # Create a compressed tar.gz archive
# with tarfile.open('data_red.tar.gz', 'w:gz') as tar:
#     tar.add('data_red', arcname=os.path.basename('data_red'))
# print('Info>> Saved reduced data as tar file')
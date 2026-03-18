"""
Python files to read dummy dataset created by data_create.py
"""

import os
import tarfile
import numpy as np
import paths

# functions
def angle_cor(x_raw, y_raw, angle):
    """
    correct rotation of data
    x_raw = raw x data
    y_raw = raw y data
    angle = anglre to be corrected
    """
    # angle for undoing rotation
    angle_opp=-angle

    # coefficients for undo rotation
    cos_a = np.cos(angle_opp)
    sin_a = np.sin(angle_opp)

    # undo rotation
    x_angle_cor = x_raw * cos_a - y_raw * sin_a
    y_angle_cor = x_raw * sin_a + y_raw * cos_a

    return x_angle_cor, y_angle_cor

# create dir for saving reduced data
final_dir=paths.data / 'red_data'
os.makedirs(final_dir, exist_ok=True)

# open raw data tarfile
tar_path=paths.data / 'data.tar.gz'
tar=tarfile.open(tar_path, 'r:gz')

# read data
exp_idx=0
while True:
    try:
        # get raw data
        txt_file_name = f'data/exp_{exp_idx}/data.txt'
        txt_file_tar = tar.extractfile(txt_file_name)
        raw_data = np.loadtxt(txt_file_tar, comments='#', dtype=float)
        raw_x=raw_data[:,2]
        raw_y=raw_data[:,3]
        # get alpha value from raw data file
        txt_file_tar = tar.extractfile(txt_file_name)
        with txt_file_tar as f:
            # Read the first two lines
            _ = f.readline()  # first line (skip)
            second_line = f.readline()  # second line
            alpha_val_str=second_line[9:]
            alpha_val=float(alpha_val_str)
        # reduce data
        red_x, red_y=angle_cor(raw_x, raw_y, alpha_val)
        # save reduced data
        # reduced data dir for exp
        final_exp_dir=f'red_exp_{exp_idx}'
        final_exp_dir=os.path.join(final_dir, final_exp_dir)
        os.makedirs(final_exp_dir, exist_ok=True)
        # reduced data file
        final_txt_file='red_data.txt'
        final_txt_file_loc=os.path.join(final_exp_dir, final_txt_file)
        red_data = np.column_stack((red_x, red_y))
        np.savetxt(final_txt_file_loc,
                   red_data, header='reduced_x reduced_y', fmt="%.6f")
        # next experiment
        exp_idx += 1
    except KeyError:
        break
# make a tar file for uploading to zenodo
# create a compressed tar.gz archive
final_tar_name=paths.data / 'red_data.tar.gz'
with tarfile.open(final_tar_name, 'w:gz') as tar:
    tar.add(final_dir, arcname=os.path.basename(paths.data / 'red_data'))

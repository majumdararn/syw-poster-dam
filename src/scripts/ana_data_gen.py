"""
Data generation script for analyzing reduced data
extraction of k and t by fitting raw data with sin(kx+t)
snakemake rule: analyzed_data
raw doi: 10.5281/zenodo.19115565
cache doi: 10.5281/zenodo.19115970
"""

import os
import tarfile
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
import paths

# functions
def sin_model(x, k, t):
    """
    y = sin(k * x + t)
    k : wave number
    t : phase
    """
    return np.sin(k * x + t)



# open analyzed data tarfile
tar_path=paths.data / 'red_data.tar.gz'
tar=tarfile.open(tar_path, 'r:gz')

# origial params
num_exp=10
k_org=np.linspace(1,6, num_exp) #[1, 2 ,6]
t_org=np.linspace(0,np.pi/5, num_exp) #[0, np.pi/5, np.pi/7]
k_fit=np.zeros_like(k_org)
t_fit=np.zeros_like(t_org)

# read reduced data for all measurements
exp_idx=0
while True:
    try:
        # get reduced data
        txt_file_name = f'red_data/red_exp_{exp_idx}/red_data.txt'
        txt_file_tar = tar.extractfile(txt_file_name)
        red_data = np.loadtxt(txt_file_tar, comments='#', dtype=float)
        x_red=red_data[:,0]
        y_red=red_data[:,1]
        # fit k, t
        initial_guess = [k_org[exp_idx], t_org[exp_idx]]  
        params, covariance = curve_fit(sin_model, x_red, y_red, p0=initial_guess)
        k_fit[exp_idx], t_fit[exp_idx] = params
        # next measurement
        exp_idx+=1
    except KeyError:
        break

# save analyzed data
final_dir=paths.data / 'ana_data'
os.makedirs(final_dir, exist_ok=True)
final_txt_file='ana_data.txt'
final_txt_file_loc=os.path.join(final_dir, final_txt_file)
red_data = np.column_stack((k_org, t_org, k_fit, t_fit))
np.savetxt(final_txt_file_loc,
            red_data, header='ang_freq(k) phase_shift(t) fitted_ang_freq(k) fitted_phase_shift(t)', fmt="%.6f")
# make a tar file for uploading to zenodo
# create a compressed tar.gz archive
final_tar_name=paths.data / 'ana_data.tar.gz'
with tarfile.open(final_tar_name, 'w:gz') as tar:
    tar.add(final_dir, arcname=os.path.basename(paths.data / 'ana_data'))

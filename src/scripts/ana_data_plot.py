"""
Plot script for plotting analyzed data
raw doi: 10.5281/zenodo.19115565
cache doi: 10.5281/zenodo.19115970
"""

import os
import tarfile
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
import paths

# def sin_model(x, k, t):
#     """
#     y = sin(k * x + t)
#     k : wave number
#     t : phase
#     """
#     return np.sin(k * x + t)

# # cwd
# print('Getting current working dir (cwd):')
# cwd=os.getcwd()
# print('cwd: ', cwd)
# # new line
# print('\n')

# # create dir for savinf reduced data
# final_dir='data_red'
# os.makedirs(final_dir, exist_ok=True)

# open tarfile for analyzed data
tar_path=paths.data / 'ana_data.tar.gz'
tar=tarfile.open(tar_path, 'r:gz')

# expected trend of k and t params
## plotted trend values are read from dataset
num_exp=10
k_org=np.linspace(1,6, num_exp)
t_org=np.linspace(0,np.pi/5, num_exp)
# initial array for fitted k and t
k_fit=np.zeros_like(k_org)
t_fit=np.zeros_like(t_org)

try:
    # read analyzed data
    txt_file_name = f'ana_data/ana_data.txt'
    txt_file_tar = tar.extractfile(txt_file_name)
    ana_data = np.loadtxt(txt_file_tar, comments='#', dtype=float)
    # expected trend values
    org_k=ana_data[:,0]
    org_t=ana_data[:,1]
    # fit values
    fit_k=ana_data[:,2]
    fit_t=ana_data[:,3]
    # plotting
    plt.figure(figsize=(8, 4))
    plt.plot(org_k, '--k', label='trend of k')
    plt.plot(fit_k,'o', label='fitted k')
    plt.plot(org_t, ':k', label='trend of t')
    plt.plot(fit_t,'*', label='fitted t')
    plt.xlabel('Measurement index [-]', fontsize=20)
    plt.ylabel('Data [A.U.]', fontsize=20)
    plt.tight_layout()
    plt.xticks(fontsize=20)
    plt.yticks(fontsize=20)
    plt.legend(fontsize=20, ncols=2)
    plt.ylim(top=9)
    plt.savefig(paths.figures / 'ana_data.pdf')
except KeyError:
    print("Analyzed data not generated")

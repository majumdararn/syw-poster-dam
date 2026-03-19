"""
Python files to read dummy dataset created by data_create.py
"""

import os
import tarfile
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
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

# def data_treat_plot(data, cur_trial='Not defined'):
#     """
#     read data and create x, y, y_noise
#     cur_trial is req for plotting
#     """
#     # data content
#     x=data[:,0]
#     y=data[:,1]
#     y_noise=data[:,2]
#     data_plot(x, y, y_noise, cur_trial)

# def data_plot(x, y, y_noise, cur_trial):
#     """
#     plot x, y; x, y_noise
#     cur_trial is req for title
#     """
#     plt.plot(x, y, label='Data')
#     plt.plot(x, y_noise, linestyle='',
#             marker='o', label='Noisy data')
#     plt.xlabel('x')
#     plt.ylabel('y')
#     plt.legend()
#     plt.title('Trial number: ' + str(cur_trial))
#     plt.show()

def sin_model(x, k, t):
    """
    y = sin(k * x + t)
    k : wave number
    t : phase
    """
    return np.sin(k * x + t)

# cwd
print('Getting current working dir (cwd):')
cwd=os.getcwd()
print('cwd: ', cwd)
# # new line
# print('\n')

# # create dir for savinf reduced data
# final_dir='data_red'
# os.makedirs(final_dir, exist_ok=True)

# open tarfile
tar_path=paths.data / 'ana_data.tar.gz'
tar=tarfile.open(tar_path, 'r:gz')

# origial params
num_exp=10
k_org=np.linspace(1,6, num_exp) #[1, 2 ,6]
t_org=np.linspace(0,np.pi/5, num_exp) #[0, np.pi/5, np.pi/7]
k_fit=np.zeros_like(k_org)
t_fit=np.zeros_like(t_org)

# read trail

try:
    # get raw data
    txt_file_name = f'ana_data/ana_data.txt'
    txt_file_tar = tar.extractfile(txt_file_name)
    ana_data = np.loadtxt(txt_file_tar, comments='#', dtype=float)
    org_k=ana_data[:,0]
    org_t=ana_data[:,1]
    fit_k=ana_data[:,2]
    fit_t=ana_data[:,3]
    plt.figure(figsize=(8, 4))
    plt.plot(org_k, '--k', label='trend of k')
    plt.plot(fit_k,'o', label='fitted k')
    plt.plot(org_t, '--k', label='trend of t')
    plt.plot(fit_t,'*', label='fitted t')
    plt.xlabel('Pixel positions [A.U.]', fontsize=20)
    plt.ylabel('Measurement index [-]', fontsize=20)
    plt.tight_layout()
    plt.xticks(fontsize=20)
    plt.yticks(fontsize=20)
    plt.legend(fontsize=20, ncols=2)
    plt.ylim(top=9)
    plt.savefig(paths.figures / 'ana_data.pdf')
    # # save reduced data
    # # reduced data dir for exp
    # final_exp_dir=f'red_exp_{exp_idx}'
    # final_exp_dir=os.path.join(final_dir, final_exp_dir)
    # os.makedirs(final_exp_dir, exist_ok=True)
    # # reduced data file
    # final_txt_file='red_data.txt'
    # final_txt_file_loc=os.path.join(final_exp_dir, final_txt_file)
    # red_data = np.column_stack((red_x, red_y))
    # np.savetxt(final_txt_file_loc,
    #             red_data, header='reduced_x reduced_y', fmt="%.6f")
    # # next experiment
    # exp_idx += 1
except KeyError:
    print("file does not exist")


# while os.path.exists(f'data_red/exp_{exp_idx}_red'):
#     print(f'exists exp data_red/exp_{exp_idx}_red')
#     print(f'reading data_red.txt from data_red/exp_{exp_idx}_red')
#     txt_file_path=f'data_red/exp_{exp_idx}_red/data_red.txt'
#     data=np.loadtxt(txt_file_path, comments='#', dtype='float')
#     x_red=data[:,0]
#     y_red=data[:,1]
#     # plt.plot(x_red,y_red,'o')
#     # Initial guesses for k, t
#     initial_guess = [k_org[exp_idx], t_org[exp_idx]]  
#     params, covariance = curve_fit(sin_model, x_red, y_red, p0=initial_guess)

#     k_fit[exp_idx], t_fit[exp_idx] = params
#     print(f"Fitted parameters:\n k = {k_fit[exp_idx]:.4f}, t = {t_fit[exp_idx]:.4f}")
#     print(f"Original parameters:\n k = {k_org[exp_idx]:.4f}, t = {t_org[exp_idx]:.4f}")
#     exp_idx+=1
# plt.plot(k_org)
# plt.plot(k_fit[0:exp_idx], 'o')
# plt.plot(t_org)
# plt.plot(t_fit[0:exp_idx], 'o')
# plt.show()
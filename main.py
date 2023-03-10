# -*- coding: utf-8 -*-
'''
Author: Rui Wang
Date: 2021-01-19 22:27:07
LastModifiedBy: Rui Wang
LastEditTime: 2021-03-28 11:26:09
Email: wangru25@msu.edu
FilePath: /45_HERMESLaplacian/main.py
Description: 
'''
import os
import numpy as np
import pandas as pd
from termcolor import colored
import HERMESLaplacian.ReadFile.ReadBfactor as ReadBfactor
import HERMESLaplacian.ReadFile.GetXYZ as GetXYZ
import HERMESLaplacian.ReadFile.GetStepFunc as GetStepFunc
import HERMESLaplacian.ReadFile.GetGudhi as GetGudhi
import HERMESLaplacian.Plot.PlotBarcode as PlotBarcode
import HERMESLaplacian.Plot.PlotStepFunc as PlotStepFunc

# proList = ['5CYT_CA_A2']
# proList = ['2HQK_CA_A2']
# proList = ['1MHP']
# proList = ['C20']
# proList = ['C60Reshape']
# proList = ['C3']
proList = ['43']

for pro_name in proList:
    print(colored('======= The structure is ' + pro_name + ' =======', 'red'))
    folder_name = pro_name

    main_dir = '/home/rui/Dropbox/Linux_Backup/MSU/1_Training/45_HERMESLaplacian'
    pro_dir = main_dir + '/Data' + '/' + folder_name
    savefig_dir = main_dir + '/Fig'
    ripser_dir = '/home/rui/Dropbox/Linux_Backup/MSU/0_Packages/ripser'

    filtration_file = 'filtration_1.txt ' # notice: There is a space
    num_eigs = '10000 '
    persistent = '0 '
    complexes = 'r'  # '' for alpha complexes and 'r' for rips complexes
    maxval = 2
    filtration = np.arange(0.0, 10.0001, 0.01)
    # filtration = np.arange(1.5, 10.001, 0.01)
    threshold = '1000'   #radius 

    # # get xyz file
    # ReadBfactor.get_bfactor_structure(pro_name, pro_dir)
    # GetXYZ.getXYZ(pro_name, pro_dir)

    os.chdir(pro_dir)
    os.system('./../../HERMES' + '/Snapshot_xyz ' + pro_dir + '/' + pro_name + '.xyz ' + pro_dir + '/' + filtration_file + num_eigs + persistent)
    # os.system('./../../Snapshot' + '/Snapshot_xyz ' + pro_dir + '/' + pro_name + '.xyz ' + pro_dir + '/' + filtration_file + num_eigs + persistent + complexes + ' ' + threshold)


    if complexes == 'r':
        method = 'Ripser'

        # change the dir to risper package
        os.chdir(ripser_dir)
        os.system('./ripser --format point-cloud --dim 2 '+ pro_dir + '/' + pro_name + '.xyz' + '>' + pro_dir + '/' + pro_name + '_Ripser.txt')
        
        PlotBarcode.getBettiMatrix(pro_name, pro_dir, method)
        PlotBarcode.plotB012Persistent(maxval, pro_name, pro_dir, savefig_dir, eval(persistent), method, complexes) ##need to add a if 
        
        GetStepFunc.combineStepFuncCompare(pro_name, filtration, pro_dir, complexes, eval(persistent), method)
        PlotStepFunc.plotB012Compare(pro_name,filtration, pro_dir, savefig_dir,complexes, eval(persistent), method)
        
        GetStepFunc.combineStepFuncSpec(pro_name,filtration,pro_dir, complexes)
        PlotStepFunc.plotSpectra(pro_name,filtration, pro_dir,savefig_dir,complexes, eval(persistent)) 

    elif complexes == 'a':
        method = 'Gudhi'

        # Run Gudhi
        GetGudhi.getGudhi(pro_name, pro_dir)

        PlotBarcode.getBettiMatrix(pro_name, pro_dir, method)
        PlotBarcode.plotB012Persistent(maxval, pro_name, pro_dir, savefig_dir, eval(persistent), method, complexes) ##need to add a if 
        
        GetStepFunc.combineStepFuncCompare(pro_name, filtration, pro_dir, complexes, eval(persistent), method)
        PlotStepFunc.plotB012Compare(pro_name,filtration, pro_dir, savefig_dir,complexes, eval(persistent), method)
        
        GetStepFunc.combineStepFuncSpec(pro_name,filtration,pro_dir, complexes)
        PlotStepFunc.plotSpectra(pro_name,filtration, pro_dir,savefig_dir,complexes, eval(persistent))








# -*- coding: utf-8 -*-
'''
Author: Rui Wang
Date: 2021-01-19 22:44:23
LastModifiedBy: Rui Wang
LastEditTime: 2021-01-19 22:44:24
Email: wangru25@msu.edu
FilePath: /45_HERMESLaplacian/HERMESLaplacian/ReadFile/ReadBfactor.py
Description: 
'''
import numpy as np

def get_bfactor_structure(pro_name, working_dir):

    profile = open(working_dir+'/'+pro_name+'.pdb')
    outname = pro_name+'.xyzr'
    writeFile = open(working_dir+'/'+outname, 'w')

    lines = profile.read().splitlines()
    for line in lines:
        _,_,_,_,_,_,x,y,z,_,b,_ = line.split()
        writeFile.write('%.3f      %.3f      %.3f      %.3f \n'%(float(x),float(y),float(z),float(b)))
    writeFile.close()
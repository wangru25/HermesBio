# -*- coding: utf-8 -*-
'''
Author: Rui Wang
Date: 2021-01-19 22:43:53
LastModifiedBy: Rui Wang
LastEditTime: 2021-01-19 22:43:53
Email: wangru25@msu.edu
FilePath: /45_HERMESLaplacian/HERMESLaplacian/ReadFile/GetXYZ.py
Description: 
'''
import os
import numpy as np


def getXYZ(xyz_name,working_dir):

    xyzfile = open(working_dir+'/'+xyz_name+'.xyzr')   #readlines will change the original file, we need to reload again
    writeFile = open(working_dir + '/' + xyz_name + '.xyz','w')
    lines = xyzfile.readlines()

    for line in lines:
        x,y,z,r = line.split()
        writeFile.write('%.7f      %.7f      %.7f\n'%(float(x),float(y),float(z)))
    writeFile.close()

# -*- coding: utf-8 -*-
'''
Author: Rui Wang
Date: 2021-01-19 22:43:17
LastModifiedBy: Rui Wang
LastEditTime: 2022-07-19 14:57:15
Email: wangru25@msu.edu
FilePath: /45_HERMESLaplacian/HERMESLaplacian/ReadFile/GetGudhi.py
Description: 
'''
import gudhi
import numpy as np


def getGudhi(name_id, working_dir):
    points = np.genfromtxt(working_dir + '/'+ name_id + '.xyz')
    print(points)
    # writeFile = open(working_dir + '/'+ name_id + '_Gudhi.txt', 'w')
    

    # from scipy.spatial import distance
    # dist = distance.cdist(points, points, 'euclidean')
    # print(np.max(dist))
    # print(np.min(dist))

    # with open(working_dir + '/' + name_id + '.dis', 'w') as testfile:
    #     for row in dist:
    #         testfile.write(' '.join([str(a) for a in row]) + '\n')

    alpha_complex = gudhi.AlphaComplex(points=points)
    PH = alpha_complex.create_simplex_tree().persistence() #PH: Persistent homology

    # writeFile.write('persistence intervals in dim 0:\n')
    for item in PH:
        print(item)
    # for item in PH:
    #     if item[0] == 0:
    #         writeFile.write('(%s,%s)\n'%(item[1][0],item[1][1]))

    # writeFile.write('persistence intervals in dim 1:\n')
    # for item in PH:
    #     if item[0] == 1:
    #         writeFile.write('(%s,%s)\n'%(item[1][0],item[1][1]))
            
    # writeFile.write('persistence intervals in dim 2:\n')
    # for item in PH:
    #     if item[0] == 2:
    #         writeFile.write('(%s,%s)\n'%(item[1][0],item[1][1]))

    # writeFile.close()


# rips complex ---> betti 0
# alpha complex ---> betti 1 and betti 2


# getGudhi('43', '/Users/rui/Dropbox/Linux_Backup/MSU/1_Training/45_HERMESLaplacian/Data/43')


getGudhi('43', '/Users/rui/Dropbox/Linux_Backup/MSU/1_Training/45_HERMESLaplacian/Data/43')

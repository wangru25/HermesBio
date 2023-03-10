# -*- coding: utf-8 -*-
'''
Author: Rui Wang
Date: 2021-01-19 22:57:15
LastModifiedBy: Rui Wang
LastEditTime: 2021-03-28 11:46:39
Email: wangru25@msu.edu
FilePath: /45_HERMESLaplacian/HERMESLaplacian/Plot/PlotBarcode.py
Description: 
'''

from matplotlib import collections as mc
import matplotlib as mpl
import pylab as plt
import numpy as np
import pandas as pd

import sys,os

# mpl.rcParams['xtick.labelsize'] = 1
# mpl.rcParams['lines.linewidth'] = 1


def getBettiMatrix(inFileName, working_dir, method):
    if method == 'Ripser':
        inFile = open(working_dir + '/' + inFileName + '_Ripser.txt')
        writeFile_0 = open(working_dir + '/' + inFileName + '_Ripser_Dim0.txt','w')
        writeFile_1 = open(working_dir + '/' + inFileName + '_Ripser_Dim1.txt','w')
        writeFile_2 = open(working_dir + '/' + inFileName + '_Ripser_Dim2.txt','w')
        lines = inFile.readlines()

        saveIndex_0 = 0
        saveIndex_1 = 0
        saveIndex_2 = 100000000
        for i in range(len(lines)):
            if 'dim 0' in lines[i]:
                saveIndex_0 = i
            elif 'dim 1' in lines[i]:
                saveIndex_1 = i
            elif 'dim 2' in lines[i]:
                saveIndex_2 = i
        for i in range(len(lines)):
            if i > saveIndex_0 and i < saveIndex_1:
                writeFile_0.write('%s'%lines[i].replace(' [','').replace(')','').replace(' ', '100000'))
            elif i > saveIndex_1 and i < saveIndex_2:
                writeFile_1.write('%s'%lines[i].replace(' [','').replace(')',''))
            elif i > saveIndex_2:
                writeFile_2.write('%s'%lines[i].replace(' [','').replace(')',''))
            # else:
            #     writeFile_2.write('0,0')
        writeFile_0.close()
        writeFile_1.close()
        writeFile_2.close()

    elif method == 'Gudhi' :
        inFile = open(working_dir + '/' + inFileName + '_%s.txt'%method)
        writeFile_0 = open(working_dir + '/' + inFileName + '_%s_Dim0.txt'%method,'w')
        writeFile_1 = open(working_dir + '/' + inFileName + '_%s_Dim1.txt'%method,'w')
        writeFile_2 = open(working_dir + '/' + inFileName + '_%s_Dim2.txt'%method,'w')
        lines = inFile.readlines()

        saveIndex_0 = 0
        saveIndex_1 = 0
        saveIndex_2 = 100000000
        for i in range(len(lines)):
            if 'dim 0' in lines[i]:
                saveIndex_0 = i
            elif 'dim 1' in lines[i]:
                saveIndex_1 = i
            elif 'dim 2' in lines[i]:
                saveIndex_2 = i
        for i in range(len(lines)):
            if i > saveIndex_0 and i < saveIndex_1:
                writeFile_0.write('%s'%lines[i].replace('(','').replace(')','').replace('inf', '100000'))
            elif i > saveIndex_1 and i < saveIndex_2:
                writeFile_1.write('%s'%lines[i].replace('(','').replace(')',''))
            elif i > saveIndex_2:
                writeFile_2.write('%s'%lines[i].replace('(','').replace(')',''))
            # else: 
            #     writeFile_2.write('0,0')

        writeFile_0.close()
        writeFile_1.close()
        writeFile_2.close()

def plotBarcodeAllPersistent(ax, DimData, maxval, name_id, dim, working_dir, persistent, complexes):
    Births = [0] # Set Deaths = [], then all of the three plots will have the same axis
    Deaths = [0] # Set Deaths = [], then all of the three plots will have the same axis
    if complexes == 'a':
        DimData = np.sqrt(DimData)
        for i in range(DimData.shape[0]):
            DimData[i,1] = DimData[i,1] - persistent

    elif complexes == 'r':
        DimData = DimData/2
        for i in range(DimData.shape[0]):
            DimData[i,1] = DimData[i,1] - persistent
    for i in range(DimData.shape[0]):
        DimData = np.where(DimData>=maxval, maxval, DimData)
        Births.append(DimData[i,0])
        Deaths.append(DimData[i,1])

    Index1 = np.argsort(Deaths)
    Index2 = np.argsort(Births)
    left = np.min(Births)
    right = np.max(Deaths)
    step = (right-left)/float(len(Births))
    start = 0.0
    lines = []
    if int(dim) == 0:
        Index = Index1
    else:
        Index = Index2
    for i in Index:
        lines.append([(Births[i],start),(Deaths[i],start)])
        lines.append([(maxval,start),(maxval,start)])
        start += step
    lc = mc.LineCollection(lines, linewidths=1.1)
    ax.add_collection(lc)
    
    ax.set_xlabel('')
    ax.set_yticks([])
    # ax.set(xlim=(0,maxval))
    ax.autoscale()
    # ax.set_ylabel('betti'+dim,fontsize=11,fontweight='bold')
    if complexes == 'a':
        ax.set_ylabel(r'$\beta^{\alpha,%.2f}_%d$'%(persistent,int(dim)),fontsize=11,fontweight='bold')
    elif complexes == 'r':
        ax.set_ylabel(r'$\beta^{r,%.2f}_%d$'%(persistent,int(dim)),fontsize=11,fontweight='bold')
    # plt.savefig(figure_dir+'/'+name_id+'_Barcode_Dim'+dim+'.pdf', dpi = 500)
    # plt.show()

def plotB012Persistent(maxval, name_id, working_dir, savefig_dir, persistent, method, complexes):
    DimData1 = pd.read_csv(working_dir+'/'+name_id+'_%s_Dim'%method+'0'+'.txt', header=None).to_numpy()
    DimData2 = pd.read_csv(working_dir+'/'+name_id+'_%s_Dim'%method+'1'+'.txt', header=None).to_numpy()
    DimData3 = pd.read_csv(working_dir+'/'+name_id+'_%s_Dim'%method+'2'+'.txt', header=None).to_numpy()
    f,(ax1,ax2,ax3) = plt.subplots(3,1,figsize=(8,5))
    plotBarcodeAllPersistent(ax1, DimData1, maxval, name_id, '0', working_dir, persistent, complexes)
    plotBarcodeAllPersistent(ax2, DimData2, maxval, name_id, '1', working_dir, persistent, complexes)
    plotBarcodeAllPersistent(ax3, DimData3, maxval, name_id, '2', working_dir, persistent, complexes)
    plt.savefig(savefig_dir+'/'+name_id+'_%s_Barcode_DimAll_%.2f.pdf'%(method,persistent), dpi = 500)
    # plt.show()
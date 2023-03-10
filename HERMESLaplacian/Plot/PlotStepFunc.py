# -*- coding: utf-8 -*-
'''
Author: Rui Wang
Date: 2021-01-19 23:11:21
LastModifiedBy: Rui Wang
LastEditTime: 2021-03-07 14:56:42
Email: wangru25@msu.edu
FilePath: /45_HERMESLaplacian/HERMESLaplacian/Plot/PlotStepFunc.py
Description: 
'''

import numpy as np
import pandas as pd
import plotly.graph_objects as go
import matplotlib.pyplot as plt
import matplotlib as mpl
import seaborn as sns



def plotStepFuncAllCompare(ax, DimData,name_id, dim, working_dir, complexes, persistent, method):
    # sns.lineplot(data=DimData, x = 'radius', y='betti%s_Snapshot'%dim, palette='rocket_r', drawstyle='steps-pre',linestyle='solid', linewidth=1, color='red', ax=ax)
    # sns.lineplot(data=DimData, x = 'radius', y='betti%s_Ripser'%dim, palette='rocket_r', drawstyle='steps-pre', linewidth=1,linestyle='solid', color='purple', ax=ax)
    sns.lineplot(data=DimData, x = 'radius', y='betti%s_Snapshot'%dim, palette='rocket_b', drawstyle='steps-pre',linestyle='dotted', linewidth=1, color='black', ax=ax)
    sns.lineplot(data=DimData, x = 'radius', y='betti%s_%s'%(dim,method), palette='rocket_b', drawstyle='steps-pre',linestyle='dotted', linewidth=1, color='green', ax=ax)
    ax.autoscale()
    ax.set_xlabel('')
    # ax.set_yticks([])
    if complexes == 'a':
        ax.set_ylabel(r'$\beta^{\alpha,%.2f}_%d$'%(persistent,int(dim)),fontsize=11,fontweight='bold')
    elif complexes == 'r':
        ax.set_ylabel(r'$\beta^{r,%.2f}_%d$'%(persistent, int(dim)),fontsize=11,fontweight='bold')
    # ax.set_ylabel(r'$\beta^{r+0}_%d$'%int(dim),fontsize=11,fontweight='bold')


def plotB012Compare(name_id,filtration, working_dir, savefig_dir,complexes,persistent, method):
    DimData0 = pd.read_csv(working_dir + '/' + name_id + '_compare_stepfunc_Dim0_%s.csv'%complexes)
    DimData1 = pd.read_csv(working_dir + '/' + name_id + '_compare_stepfunc_Dim1_%s.csv'%complexes)
    DimData2 = pd.read_csv(working_dir + '/' + name_id + '_compare_stepfunc_Dim2_%s.csv'%complexes)
    f,(ax1,ax2,ax3) = plt.subplots(3,1,figsize=(8,5))
    # f,ax1 = plt.subplots(figsize=(7,3))
    plotStepFuncAllCompare(ax1, DimData0, name_id, '0', working_dir, complexes,persistent, method)
    plotStepFuncAllCompare(ax2, DimData1, name_id, '1', working_dir, complexes,persistent, method)
    plotStepFuncAllCompare(ax3, DimData2, name_id, '2', working_dir, complexes,persistent, method)
    plt.savefig(savefig_dir+'/'+name_id+'_Stepfunc_DimAll_Compare_%.2f_%s.pdf'%(persistent,complexes), dpi = 500)
    # plt.show()



def plotSpectraAll(ax, DimData,name_id, dim, working_dir, complexes, persistent):
    ax.autoscale()
    # ax.set_yticks([])
    ax2 = ax.twinx()
    ax.autoscale()

    if persistent == 0:
        color1 = 'blue'
        color2 = 'red'
    else:
        color1 = 'green'
        color2 = 'orange'
    
    sns.lineplot(data=DimData, x = 'radius', y='betti%s_Snapshot'%dim, palette='rocket_r', drawstyle='steps-pre',linestyle='solid', linewidth=1, color='%s'%color1, ax=ax)
    sns.lineplot(data=DimData, x = 'radius', y='spec%s_Snapshot'%dim, palette='rocket_b', drawstyle='steps-pre',linestyle='solid', linewidth=1, color='%s'%color2, ax=ax2)
    if complexes == 'a':
        ax.set_ylabel(r'$\beta^{\alpha,%.2f}_%d$'%(persistent, int(dim)),fontsize=11,fontweight='bold',color='%s'%color1)
        ax2.set_ylabel(r'$\lambda^{\alpha,%.2f}_%d$'%(persistent, int(dim)),fontsize=11,fontweight='bold',color='%s'%color2)
    elif complexes == 'r':
        ax.set_ylabel(r'$\beta^{r,%.2f}_%d$'%(persistent, int(dim)),fontsize=11,fontweight='bold',color='%s'%color1)
        ax2.set_ylabel(r'$\lambda^{r,%.2f}_%d$'%(persistent, int(dim)),fontsize=11,fontweight='bold',color='%s'%color2)
    # ax.set_ylabel(r'$\beta^{r+0}_%d$'%int(dim),fontsize=11,fontweight='bold')
    ax.set_xlabel('')
    ax2.set_xlabel('')

    for line in ax.yaxis.get_ticklines():
        line.set_color('%s'%color1)
    for line in ax2.yaxis.get_ticklines():
        line.set_color('%s'%color2)

    for label in ax.yaxis.get_ticklabels():
        label.set_color('%s'%color1)
    for label in ax2.yaxis.get_ticklabels():
        label.set_color('%s'%color2)


def plotSpectra(name_id,filtration, working_dir, savefig_dir,complexes, persistent):
    DimData0 = pd.read_csv(working_dir + '/' + name_id + '_spectra_stepfunc_Dim0_%s.csv'%complexes)
    DimData1 = pd.read_csv(working_dir + '/' + name_id + '_spectra_stepfunc_Dim1_%s.csv'%complexes)
    DimData2 = pd.read_csv(working_dir + '/' + name_id + '_spectra_stepfunc_Dim2_%s.csv'%complexes)
    f,(ax1,ax2,ax3) = plt.subplots(3,1,figsize=(8,5))
    # f,ax2 = plt.subplots(figsize=(8,2.5))
    plotSpectraAll(ax1, DimData0, name_id, '0', working_dir, complexes, persistent)
    plotSpectraAll(ax2, DimData1, name_id, '1', working_dir, complexes, persistent)
    plotSpectraAll(ax3, DimData2, name_id, '2', working_dir, complexes, persistent)
    plt.savefig(savefig_dir+'/'+name_id+'_Stepfunc_DimAll_Spectra_%.2f_%s.pdf'%(persistent,complexes), dpi = 500)
    # plt.show()
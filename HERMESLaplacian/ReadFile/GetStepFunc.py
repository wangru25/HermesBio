# -*- coding: utf-8 -*-
'''
Author: Rui Wang
Date: 2021-01-19 23:16:51
LastModifiedBy: Rui Wang
LastEditTime: 2021-03-04 14:45:04
Email: wangru25@msu.edu
FilePath: /45_HERMESLaplacian/HERMESLaplacian/ReadFile/GetStepFunc.py
Description: 
'''


import numpy as np
import pandas as pd

def generateFromSnapshot(filtration, working_dir):
    b0FileSnap = open(working_dir + '/' + 'snapshots_vertex.txt'); lines_0 = b0FileSnap.readlines()
    b1FileSnap = open(working_dir + '/' + 'snapshots_edge.txt'); lines_1 = b1FileSnap.readlines()
    b2FileSnap = open(working_dir + '/' + 'snapshots_facet.txt'); lines_2 = b2FileSnap.readlines()

    saveList0_Snap = []; saveList1_Snap = []; saveList2_Snap = []   

    for item, line in enumerate(lines_0):
        if len(line) == 1:
            betti0 = 0
        elif len(line) == 3:
            if eval(line.replace(' \n','').replace(' ',',')) < 0.0001:
                betti0 = 1
            else: 
                betti0 = 0
        else:
            tmpVal0 = list(eval(line.replace(' \n','').replace(' ',',')))
            betti0 = np.sum(list(map(lambda tmpVal0: tmpVal0<0.0001, tmpVal0)))
        saveList0_Snap.append(betti0)
        

    for item, line in enumerate(lines_1):
        if len(line) == 1:
            betti1 = 0
        elif len(line) == 3:
            if eval(line.replace(' \n','').replace(' ',',')) < 0.0001:
                betti1 = 1
            else: 
                betti1 = 0
        else:        
            tmpVal1 = list(eval(line.replace(' \n','').replace(' ',',')))
            betti1 = np.sum(list(map(lambda tmpVal1: tmpVal1<0.0001, tmpVal1)))
        saveList1_Snap.append(betti1)

    for item, line in enumerate(lines_2):
        if len(line) == 1:
            betti2 = 0
        elif len(line) == 3:
            if eval(line.replace(' \n','').replace(' ',',')) < 0.0001:
                betti2 = 1
            else: 
                betti2 = 0
        else:
            tmpVal2 = list(eval(line.replace(' \n','').replace(' ',',')))
            betti2 = np.sum(list(map(lambda tmpVal2: tmpVal2<0.0001, tmpVal2)))
        saveList2_Snap.append(betti2)

    return saveList0_Snap,saveList1_Snap,saveList2_Snap


def getSpectraFromSnapshot(filtration, working_dir):
    b0FileSnap = open(working_dir + '/' + 'snapshots_vertex.txt'); lines_0 = b0FileSnap.readlines()
    b1FileSnap = open(working_dir + '/' + 'snapshots_edge.txt'); lines_1 = b1FileSnap.readlines()
    b2FileSnap = open(working_dir + '/' + 'snapshots_facet.txt'); lines_2 = b2FileSnap.readlines()

    saveList0_Spec = []; saveList1_Spec = []; saveList2_Spec = []   

    for item, line in enumerate(lines_0):
        if len(line) == 1:
            spec0 = 0
        elif len(line) == 3:
            if eval(line.replace(' \n','').replace(' ',',')) < 0.0001:
                spec0 = 0
        else:
            tmpVal0 = np.asarray(list(eval(line.replace(' \n','').replace(' ',','))))
            tmpVal0 = np.where(tmpVal0<0.0001,0,tmpVal0)
            tmpList0 = []
            for idx in range(len(tmpVal0)):
                if tmpVal0[idx] != 0.0:
                    tmpList0.append(tmpVal0[idx])
            if len(tmpList0) == 0:
                spec0 = 0
            else:
                spec0 = np.min(np.asarray(tmpList0))
        saveList0_Spec.append(spec0)

    for item, line in enumerate(lines_1):
        if len(line) == 1:
            spec1 = 0
        elif len(line) == 3:
            if eval(line.replace(' \n','').replace(' ',',')) < 0.0001:
                spec1 = 0
        else:
            tmpVal1 = np.asarray(list(eval(line.replace(' \n','').replace(' ',','))))
            tmpVal1 = np.where(tmpVal1<0.0001,0,tmpVal1)
            tmpList1 = []
            for idx in range(len(tmpVal1)):
                if tmpVal1[idx] != 0.0:
                    tmpList1.append(tmpVal1[idx])
            if len(tmpList1) == 0:
                spec1 = 0
            else:
                spec1 = np.min(np.asarray(tmpList1))
        saveList1_Spec.append(spec1)

    for item, line in enumerate(lines_2):
        if len(line) == 1:
            spec2 = 0
        elif len(line) == 3:
            if eval(line.replace(' \n','').replace(' ',',')) < 0.0001:
                spec2 = 0
        else:
            tmpVal2 = np.asarray(list(eval(line.replace(' \n','').replace(' ',','))))
            tmpVal2 = np.where(tmpVal2<0.0001,0,tmpVal2)
            tmpList2 = []
            for idx in range(len(tmpVal2)):
                if tmpVal2[idx] != 0.0:
                    tmpList2.append(tmpVal2[idx])
            if len(tmpList2) == 0:
                spec2 = 0
            else:
                spec2 = np.min(np.asarray(tmpList2))
        saveList2_Spec.append(spec2)

    return saveList0_Spec,saveList1_Spec,saveList2_Spec


def generateFromPersistent(name_id, filtration, complexes, persistent, working_dir, method):

    b0File_Gud = pd.read_csv(working_dir+'/'+name_id+'_%s_Dim'%method+'0'+'.txt', header=None).to_numpy()
    b1File_Gud = pd.read_csv(working_dir+'/'+name_id+'_%s_Dim'%method+'1'+'.txt', header=None).to_numpy()
    b2File_Gud = pd.read_csv(working_dir+'/'+name_id+'_%s_Dim'%method+'2'+'.txt', header=None).to_numpy()
    
    if complexes == 'a':
        b0File_Gud = np.sqrt(b0File_Gud)
        for i in range(b0File_Gud.shape[0]):
            if b0File_Gud[i,1] - persistent <= b0File_Gud[i,0]:
                b0File_Gud[i,1] = 0
                b0File_Gud[i,0] = 0
            else:
                b0File_Gud[i,1] = b0File_Gud[i,1] - persistent
                
        b1File_Gud = np.sqrt(b1File_Gud)

        for i in range(b1File_Gud.shape[0]):
            if b1File_Gud[i,1] - persistent <= b1File_Gud[i,0]:
                b1File_Gud[i,1] = 0
                b1File_Gud[i,0] = 0
            else:
                b1File_Gud[i,1] = b1File_Gud[i,1] - persistent

        b2File_Gud = np.sqrt(b2File_Gud)

        for i in range(b2File_Gud.shape[0]):
            if b2File_Gud[i,1] - persistent <= b2File_Gud[i,0]:
                b2File_Gud[i,1] = 0
                b2File_Gud[i,0] = 0
            else:
                b2File_Gud[i,1] = b2File_Gud[i,1] - persistent

        b0File_Gud = b0File_Gud**2
        b1File_Gud = b1File_Gud**2
        b2File_Gud = b2File_Gud**2

        
    elif complexes == 'r':
        b0File_Gud = b0File_Gud/2
        for i in range(b0File_Gud.shape[0]):
            if b0File_Gud[i,1] - persistent <= b0File_Gud[i,0]:
                b0File_Gud[i,1] = 0
                b0File_Gud[i,0] = 0
            else:
                b0File_Gud[i,1] = b0File_Gud[i,1] - persistent
        b1File_Gud = b1File_Gud/2
        for i in range(b1File_Gud.shape[0]):
            if b1File_Gud[i,1] - persistent <= b1File_Gud[i,0]:
                b1File_Gud[i,1] = 0
                b1File_Gud[i,0] = 0
            else:
                b1File_Gud[i,1] = b1File_Gud[i,1] - persistent
        
        b2File_Gud = b2File_Gud/2
        for i in range(b2File_Gud.shape[0]):
            if b2File_Gud[i,1] - persistent <= b2File_Gud[i,0]:
                b2File_Gud[i,1] = 0
                b2File_Gud[i,0] = 0
            else:
                b2File_Gud[i,1] = b2File_Gud[i,1] - persistent

        b0File_Gud = (b0File_Gud*2)
        b1File_Gud = (b1File_Gud*2)
        b2File_Gud = (b2File_Gud*2)

    saveList0_Gud = []; saveList1_Gud = []; saveList2_Gud = []
    
    for item in filtration:
        item_fix = np.round(item, 2)
        factor = np.array([[1],[1]])
        
        if b0File_Gud.shape[0] != 0:
            newMatrix = np.where(b0File_Gud<item_fix, 0, b0File_Gud) @ factor
            betti0 = newMatrix[newMatrix != 0].shape[0]
        else:
            betti0 = 0
        saveList0_Gud.append(betti0)

        if b1File_Gud.shape[0] != 0:
            tmpMatrix1 = np.where(b1File_Gud[:,0].reshape(-1,1)<=item_fix, b1File_Gud, 0)
            newMatrix1 = np.where(b1File_Gud[:,1].reshape(-1,1)>=item_fix, tmpMatrix1, 0) @ factor
            betti1 =  newMatrix1[newMatrix1 != 0].shape[0]
        else:
            betti1 = 0
        saveList1_Gud.append(betti1)

        if b2File_Gud.shape[0] != 0:
            tmpMatrix2 = np.where(b2File_Gud[:,0].reshape(-1,1)<=item_fix, b2File_Gud, 0)
            newMatrix2 = np.where(b2File_Gud[:,1].reshape(-1,1)>=item_fix, tmpMatrix2, 0) @ factor
            betti2 =  newMatrix2[newMatrix2 != 0].shape[0]
        else:
            betti2 = 0
        saveList2_Gud.append(betti2)

    return saveList0_Gud, saveList1_Gud, saveList2_Gud


def combineStepFuncCompare(name_id, filtration, working_dir, complexes, persistent, method):

    saveList0_Snap,saveList1_Snap,saveList2_Snap = generateFromSnapshot(filtration, working_dir)
    saveList0_Gud, saveList1_Gud, saveList2_Gud = generateFromPersistent(name_id, filtration, complexes, persistent, working_dir, method)
    print(len(saveList2_Snap))
    print(len(saveList2_Gud))

    writeFile_0 = open(working_dir + '/' + name_id + '_compare_stepfunc_Dim0_%s.csv'%complexes, 'w'); writeFile_0.write('radius,betti0_Snapshot,betti0_%s\n'%method)
    writeFile_1 = open(working_dir + '/' + name_id + '_compare_stepfunc_Dim1_%s.csv'%complexes, 'w'); writeFile_1.write('radius,betti1_Snapshot,betti1_%s\n'%method)
    writeFile_2 = open(working_dir + '/' + name_id + '_compare_stepfunc_Dim2_%s.csv'%complexes, 'w'); writeFile_2.write('radius,betti2_Snapshot,betti2_%s\n'%method)

    for item,radius in enumerate(filtration):
        if complexes == 'a':
            radius = np.sqrt(radius)
        elif complexes == 'r':
            radius = radius
        writeFile_0.write('%.4f,%d,%d\n'%(radius,saveList0_Snap[item],saveList0_Gud[item]))
        writeFile_1.write('%.4f,%d,%d\n'%(radius,saveList1_Snap[item],saveList1_Gud[item]))
        writeFile_2.write('%.4f,%d,%d\n'%(radius,saveList2_Snap[item],saveList2_Gud[item]))


def combineStepFuncSpec(name_id, filtration, working_dir, complexes):

    saveList0_Snap,saveList1_Snap,saveList2_Snap = generateFromSnapshot(filtration, working_dir)
    saveList0_Spec,saveList1_Spec,saveList2_Spec = getSpectraFromSnapshot(filtration, working_dir)

    writeFile_0 = open(working_dir + '/' + name_id + '_spectra_stepfunc_Dim0_%s.csv'%complexes, 'w'); writeFile_0.write('radius,betti0_Snapshot,spec0_Snapshot\n')
    writeFile_1 = open(working_dir + '/' + name_id + '_spectra_stepfunc_Dim1_%s.csv'%complexes, 'w'); writeFile_1.write('radius,betti1_Snapshot,spec1_Snapshot\n')
    writeFile_2 = open(working_dir + '/' + name_id + '_spectra_stepfunc_Dim2_%s.csv'%complexes, 'w'); writeFile_2.write('radius,betti2_Snapshot,spec2_Snapshot\n')

    for item,radius in enumerate(filtration):
        if complexes == 'a':
            radius = np.sqrt(radius)
        elif complexes == 'r':
            radius = radius/2
        writeFile_0.write('%.4f,%d,%.4f\n'%(radius,saveList0_Snap[item],saveList0_Spec[item]))
        writeFile_1.write('%.4f,%d,%.4f\n'%(radius,saveList1_Snap[item],saveList1_Spec[item]))
        writeFile_2.write('%.4f,%d,%.4f\n'%(radius,saveList2_Snap[item],saveList2_Spec[item]))
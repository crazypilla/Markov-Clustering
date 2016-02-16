# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.


__date__ = "$7 Nov, 2015 2:07:30 AM$"
__author__ = "Harshita V"

import numpy as np
import math
from sets import Set
import datetime

def normalize(matrix):
    sum = matrix.sum(axis=0)
    return matrix/sum[np.newaxis,:]

def expansion(matrix,exp):
    return np.linalg.matrix_power(matrix,exp)

def inflation(matrix, inf):
    matrix = np.power(matrix,inf)
    return normalize(matrix)


def getclusters(matrix):
    clus = {}
    for i in range(len(matrix)):
        if matrix[i][i] != 0.0:
            for j in range(len(matrix)):
                if matrix[i][j] != 0.0 and j!=i:
                    clus[j] = i

    return clus

def getdata(fname):
    file = open(fname,'rb').readlines()
    m = {}
    i=0
    for elem in file:
        s = elem.split()
        if s[0] not in m:
            m[s[0]] = i
            i += 1
        if s[1] not in m:
            m[s[1]] = i
            i += 1

    matrix =  np.zeros((i,i))
    for elem in file:
        s = elem.split()
        matrix[m[s[0]]][m[s[1]]] = 1
        matrix[m[s[1]]][m[s[0]]] = 1

    for i in range (0,len(matrix)):
        matrix[i][i] = 1

    return matrix

if __name__ == '__main__':
    fname = raw_input("Enter file name with complete path")
    matrix = getdata(fname)
    matrix =  normalize(matrix)
    exp = int(raw_input("Enter expansion value\n"))
    inf = float(raw_input("Enter inflation value\n"))
    i = 0
    while(1):
        i += 1
        prev = matrix.copy()
        matrix = expansion(matrix,exp)
        matrix = inflation(matrix,inf)
        i += 1
        if (matrix - prev).sum() == 0.0:
            break

    cluster = getclusters(matrix)

    fname = fname[:-4] + ".clu"
    clus_file = open((fname),'w')
    size = len(matrix)
    clus_file.write("*Vertices "+str(size)+"\n")

    for i in range(size):
        if i not in cluster:
            clus_file.write(str(i)+"\n")
        else:
            clus_file.write(str(cluster[i])+"\n")
    clus_file.close()

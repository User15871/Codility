# -*- coding: utf-8 -*-
"""
Created on Sat Jul 14 14:10:55 2018

@author: andy
"""

def solution1(A):
    # write your code in Python 3.6
    sumA=[A[i]+A[i+1] for i in range(len(A)-1)]
    return(sumA.index(min(sumA)))
    pass

def solution2(A):
    # write your code in Python 3.6
    minMean=100001
    l=len(A)
    for i in range(l-1):
        sumA=A[i]+A[i+1]
        meanA=sumA/2
        if meanA < minMean:
            minP = i
            minMean = meanA
        
        if i < l-2 :
            sumA+=A[i+2]
            meanA=sumA/3
            if meanA < minMean:
                minP = i
                minMean = meanA
    return(minP)
    pass

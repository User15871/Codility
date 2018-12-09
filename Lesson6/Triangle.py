# -*- coding: utf-8 -*-
"""
Created on Sun Jul 15 11:59:56 2018

@author: andy
"""

def solution(A):
    # write your code in Python 3.6
    A.sort()
    for i in range(len(A)-2):
        if A[i]+A[i+1]>A[i+2]:
            return(1)
    return(0)
    pass
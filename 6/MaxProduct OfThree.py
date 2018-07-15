# -*- coding: utf-8 -*-
"""
Created on Sat Jul 14 21:25:58 2018

@author: andy
"""

def solution(A):
    # write your code in Python 3.6
    l=len(A)-1
    A.sort()
    return(max(A[0]*A[1]*A[l],A[l-2]*A[l-1]*A[l]))
    pass
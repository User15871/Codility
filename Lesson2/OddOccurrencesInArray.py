# -*- coding: utf-8 -*-
"""
Created on Thu Jul 12 09:33:16 2018

@author: andy
"""

def solution1(A):
    # write your code in Python 3.6
    sol=0
    for x in (A):
        sol^=x
    return(sol)
    pass

def solution2(A):
    # write your code in Python 3.6
    A.sort()
    l=len(A)-1
    for i in range(0,l,2):
        if A[i]!=A[i+1]:
            return(A[i])
    return(A[l])
    pass



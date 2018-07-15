# -*- coding: utf-8 -*-
"""
Created on Thu Jul 12 09:59:49 2018

@author: andy
"""

def solution1(A):
    # write your code in Python 3.6
    return(list(set(range(len(A)+2))-set(A))[1])
    pass

def solutio2(A):
    # write your code in Python 3.6
    l=len(A)
    return((l+1)*(l+2)//2-sum(A))
    pass
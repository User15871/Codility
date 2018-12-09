# -*- coding: utf-8 -*-
"""
Created on Thu Jul 12 09:30:50 2018

@author: andy
"""

def solution(A, K):
    # write your code in Python 3.6
    l=len(A)
    return[A[i-K%l] for i in range(l) ]
    pass
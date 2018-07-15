# -*- coding: utf-8 -*-
"""
Created on Fri Jul 13 20:38:02 2018

@author: andy
"""

def solution1(X, A):
    # write your code in Python 3.6
    sol=[A.index(i) for i in range(1,X+1)]
    return(max(sol))
    pass

def solution2(X, A):
    # write your code in Python 3.6
    compare=set(range(1,X+1))
    B=set()
    for i in range(len(A)):
        B|=set(A[i:i+1])
        if compare==B:
            return(i)
    return(-1)
        
    pass

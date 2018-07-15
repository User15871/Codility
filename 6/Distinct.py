# -*- coding: utf-8 -*-
"""
Created on Sat Jul 14 20:27:42 2018

@author: andy
"""

def solution1(A):
    # write your code in Python 3.6
    return(len(set(A)))
    pass

def solution2(A):
    l=len(A)
    if l == 0:
        distinct = 0
    else:
        distinct = 1
        A.sort()
        for i in range(l-1):
            if A[i] == A[i+1]:
                # The same element as the previous one
                continue
            else:
                # A new element
                distinct += 1
 
    return distinct
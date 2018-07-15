# -*- coding: utf-8 -*-
"""
Created on Sat Jul 14 09:38:11 2018

@author: andy
"""

def solution(A):
    # write your code in Python 3.6
    add=0
    sol=0
    for x in A:
        if x==0:
            add+=1
        else:
            sol+=add
            if sol>1e9:
                return(-1)
    return(sol)
    pass
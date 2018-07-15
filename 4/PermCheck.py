# -*- coding: utf-8 -*-
"""
Created on Fri Jul 13 20:24:43 2018

@author: andy
"""

def solution1(A):
    # write your code in Python 3.6
    if set(A)==set(range(1,len(A)+1)):
        return(1)
    else:
        return(0)
    pass

def solution2(A):
    # write your code in Python 3.6
    Amax=max(A)
    l=len(A)
    if Amax!=l:
        return(0)
    sol=[0]*(Amax+1)
    for x in A:
        sol[x]=1
    if sum(sol)==Amax:
        return(1)
    else:
        return(0)
    pass
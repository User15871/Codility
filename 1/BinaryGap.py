# -*- coding: utf-8 -*-
"""
Created on Thu Jul 12 09:28:03 2018

@author: andy
"""

def solution(N):
    # write your code in Python 3.6
    sol=[]
    a=1
    while N>0:
        if N%2==1:
            sol.append(a)
        N=N//2
        a+=1
    l=len(sol)
    if l<2:
        return(0)
    else:
        diff=[sol[i+1]-sol[i] for i in range(l-1)]
        return(max(diff)-1)
    pass
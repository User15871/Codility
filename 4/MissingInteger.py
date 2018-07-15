# -*- coding: utf-8 -*-
"""
Created on Fri Jul 13 20:53:25 2018

@author: andy
"""

def solution1(A):
    # write your code in Python 3.6
    sol=1
    while True:
        if sol in A:
            sol+=1
        else:
            return(sol)
    pass

def solutio2(A):
    # write your code in Python 3.6
    Amax=max(A)
    if Amax<1:
        return(1)
    sol=list(set(range(1,Amax+1))-set(A))
    if sol==[]:
        return(Amax+1)
    else:
        return(sol[0])
    pass

def solution3(A):
    # write your code in Python 2.7
    N=len(A)
    sol=[0]*(N+2)
    sol[0]=1
    for x in A:
        if 0<x<=N:
            sol[x]+=1
    return(sol.index(0))
    pass
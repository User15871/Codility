# -*- coding: utf-8 -*-
"""
Created on Fri Jul 13 22:13:07 2018

@author: andy
"""

def solution1(N, A):
    # write your code in Python 3.6
    N1=N+1
    counter=[0]*N1
    for x in A:
        if x==N1:
            counter=[max(counter)]*N1
        else:
            counter[x]+=1
    return(counter[1:])
    pass

def solution2(N, A):
    # write your code in Python 3.6
    N1=N+1
    counter=[0]*N1
    counterMax=0
    for x in A:
        if x==N1:
            counter=[counterMax]*N1
        else:
            counter[x]+=1
            counterMax=max(counterMax,counter[x])
    return(counter[1:])
    pass

def solution3(N, A):
    # write your code in Python 3.6
    N1=N+1
    counter=[0]*N1
    counterMax=0
    i=0
    for x in A:
        if x==N1 :
            if i==1:
                counter=[counterMax]*N1
        else:
            i=1
            counter[x]+=1
            counterMax=max(counterMax,counter[x])
    return(counter[1:])
    pass
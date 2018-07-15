# -*- coding: utf-8 -*-
"""
Created on Sat Jul 14 11:03:19 2018

@author: andy
"""

def solution1(S, P, Q):
    # write your code in Python 3.6
       
    def findMin(A):
        if "A" in A:
            return(1)
        if "C" in A:
            return(2)
        if "G" in A:
            return(3)
        if "T" in A:
            return(4)        
        
    return([findMin(set(S[P[i]:(Q[i]+1)])) for i in range(len(P))])
    pass

def decide(x,y):
    if A[y]-A[x]>0:
        return(1)
    elif C[y]-C[x]>0:
        return(2)
    elif G[y]-G[x]>0:
        return(3)
    else:
        return(4)

def solution2(S, P, Q):
    # write your code in Python 3.6
    
    global A
    global C
    global G
    l=len(S)
    l1=l+1
    A=[0]*l1
    C=[0]*l1
    G=[0]*l1
    a=0
    c=0
    g=0
    i=0
    
    while i < l:
        if S[i]=="A":
            a+=1
        elif S[i]=="C":
            c+=1
        elif S[i]=="G":
            g+=1
        i+=1
        A[i]=a
        C[i]=c
        G[i]=g
    
    return([decide(P[i],Q[i]+1) for i in range(len(P))])
    
    pass
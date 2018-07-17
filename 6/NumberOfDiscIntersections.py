# -*- coding: utf-8 -*-
"""
Created on Sun Jul 15 22:33:28 2018

@author: andy
"""

def solution1(A):
    # write your code in Python 3.6
    l=len(A)
    B=[i-A[i] for i in range(l)]
    count=0
    for i in range(l-1):
        for j in range(i+1,l):
            if A[i]+i>=B[j]:
                count+=1
                if count>1e7:
                    return(-1)
    return(count)
    pass


def solution2(A):
    # write your code in Python 3.6
    
    l=len(A)
    lowerA=[i-A[i] for i in range(l)]
    upperA=[i+A[i] for i in range(l)]
    lowerA.sort()
    upperA.sort()
    j=0
    sol=0
        
    for i in range(l):
        while j < l and upperA[i] >= lowerA[j]:
            j+=1
        sol+=j-i-1
        if sol>1e7:
            return(-1)    
    
    return(sol)
    
    pass

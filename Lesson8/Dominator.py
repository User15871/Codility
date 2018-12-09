# -*- coding: utf-8 -*-
"""
Created on Mon Jul 16 22:04:32 2018

@author: andy
"""

import math
def solution(A):
    # write your code in Python 3.6
    l=len(A)
    if l==0:
        return(-1)
    record=A[0]
    count=1
    sol=0
    
    for i in range(1,l):
        if record==A[i]:
            count+=1
        else:
            if count==0:
                record=A[i]
                sol=i
            else:
                count-=1
    if A.count(record)<=math.floor(l/2):
        return(-1)
    return(sol)
    pass
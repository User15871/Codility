# -*- coding: utf-8 -*-
"""
Created on Tue Jul 17 09:37:57 2018

@author: andy
"""

import math
def solution(A):
    # write your code in Python 3.6
    l=len(A)
    record=A[0]
    count=1
    sol=0
    for i in range(1,l):
        if record==A[i]:
            count+=1
        else:
            if count==0:
                record=A[i]
            else:
                count-=1
    total=A.count(record)
    subTotal=0
    for i in range(l):
        if A[i]==record:
            subTotal+=1
            total-=1
        if subTotal>math.floor((i+1)/2) and total>math.floor((l-i-1)/2):
            sol+=1
        
    return(sol)
    pass
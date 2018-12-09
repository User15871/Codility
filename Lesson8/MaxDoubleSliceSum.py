# -*- coding: utf-8 -*-
"""
Created on Wed Aug 15 12:38:34 2018

@author: User
"""


def solution(A):
    # write your code in Python 3.6
    sumA=0
    maxA=0
    remove=1
    record=0
    for i in range(1,len(A)-1):
        sumA+=A[i]
        if A[i]<=A[remove]:
            if record<0:
                sumA-=record
            remove=i
            record=sumA
            print(record)
        maxA=max(maxA,sumA-A[remove])
    print(A)
    return(maxA)
    pass

def solution2(A):
    # write your code in Python 3.6
    sumA=0
    maxA=0
    remove=1
    record=0
    for i in range(1,len(A)-1):
        sumA+=A[i]
        if A[i]<=A[remove]:
            if record<0:
                sumA-=record
                record=0
            remove=i
        maxA=max(maxA,sumA-A[remove])
        record=min(record,sumA)
    return(maxA)
    pass

def solution3(A):
    # write your code in Python 3.6
    left=0
    right=0
    sumA=0
    for i in range(2,len(A)-1):
        left=max(left+A[i-1],A[i-1])
        right=max(right+A[i],A[i],left)
        if right>sumA:
            sumA=right
    return(sumA)
    pass
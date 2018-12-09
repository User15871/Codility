# -*- coding: utf-8 -*-
"""
Created on Thu Jul 12 15:35:10 2018

@author: andy
"""

def solution1(A):
    # write your code in Python 3.6
    return(min([abs(sum(A[:i])-sum(A[i:])) for i in range(1,len(A))]))
    pass

def solution2(A):
    # write your code in Python 3.6
    s1=sum(A)
    s=0
    sol=abs(s1)
    for i in range(len(A)):
        s=s+A[i]
        sol=min(sol,abs(s1-2*s))
    return(sol)
    pass

def solution3(A):
    # write your code in Python 3.6
    diff=sum(A[1:])-A[0]
    sol=abs(diff)
    for i in range(1,len(A)-1):
        diff=diff-2*A[i]
        sol=min(sol,abs(diff))
    return(sol)
    pass
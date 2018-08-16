# -*- coding: utf-8 -*-
"""
Created on Thu Aug 16 16:03:04 2018

@author: User
"""

def solution(N):
    # write your code in Python 3.6
    if N==1:
        return(1)
    i=2
    count=2
    while i**2<N:
        if N%i==0:
            count+=2
        i+=1
    if i**2==N:
        count+=1
    return(count)
    pass
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 16 16:15:13 2018

@author: User
"""

def solution(N):
    # write your code in Python 3.6
    i=1
    while i**2<=N:
        if N%i==0:
            j=i
        i+=1
    return(int((j+N/j)*2))
    pass

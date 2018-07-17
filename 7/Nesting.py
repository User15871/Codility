# -*- coding: utf-8 -*-
"""
Created on Mon Jul 16 14:33:57 2018

@author: andy
"""

def solution(S):
    # write your code in Python 3.6
    count=0
    for x in S:
        if x=="(":
            count+=1
        else:
            count-=1
        if count<0:
            return(0)
    if count==0:
        return(1)
    else:
        return(0)
    pass
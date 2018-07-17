# -*- coding: utf-8 -*-
"""
Created on Mon Jul 16 14:40:58 2018

@author: andy
"""

def solution(S):
    # write your code in Python 3.6
    storage=[]
    for x in S:
        if x=="(" or x=="{" or x=="[":
            storage.append(x)
        else:
            if len(storage)==0:
                return(0)
            y=storage.pop()
            if x==")" and y!="(":
                return(0)
            if x=="}" and y!="{":
                return(0)
            if x=="]" and y!="[":
                return(0)
    if len(storage)!=0:
        return(0)
    return(1)
    pass
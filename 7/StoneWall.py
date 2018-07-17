# -*- coding: utf-8 -*-
"""
Created on Mon Jul 16 21:48:55 2018

@author: andy
"""

def solution(H):
    # write your code in Python 3.6
    Storage=[]
    check=H[0]
    count=1
    for x in H[1:]:
        
        while check>x:
            if len(Storage)==0:
                check=x
                count+=1
            else:
                check=Storage.pop()
        if check<x:
            Storage.append(check)
            check=x
            count+=1
    return(count)
    pass
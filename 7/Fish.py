# -*- coding: utf-8 -*-
"""
Created on Mon Jul 16 15:22:34 2018

@author: andy
"""

def solution(A, B):
    # write your code in Python 3.6
    down=[]
    count=0
    for i in range(len(A)):
        if B[i]==0:
            while len(down)!=0:
                fish=down.pop()
                if fish>A[i]:
                    down.append(fish)
                    break
            else:
                count+=1
        else:
            down.append(A[i])
    return(count+len(down))
    pass
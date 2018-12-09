# -*- coding: utf-8 -*-
"""
Created on Thu Aug 16 21:39:40 2018

@author: User
"""

def solution(A):
    # write your code in Python 3.6
    l=len(A)
    peaks=[]
    for i in range(1,l-1):
        if A[i+1]<A[i] and A[i-1]<A[i]:
            peaks.append(i)
    
    count=len(peaks)
    if count<=1:
        return(count)
    j=2    
    while j<=count:
        choose=peaks[0]
        flagCount=1
        for peak in peaks[1:]:
            if peak-choose>=j:
                flagCount+=1
                choose=peak
                if flagCount==j:
                    break
        if flagCount<j:
            return(j-1)
        j+=1
    return(j-1)
    pass
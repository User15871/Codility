# -*- coding: utf-8 -*-
"""
Created on Thu Aug 16 21:04:17 2018

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
    
    if count==0:
        return(0)
    
    while count>=1:
        if l%count==0:
            checkList=[False]*count
            
            groupNum=l/count
            for peak in peaks:
                checkList[int(peak//groupNum)]=True
            TrueCount=0
            for check in checkList:
                if check==False:
                    break
                TrueCount+=1
            if TrueCount==count:
                return(count)
        count-=1
    
    pass
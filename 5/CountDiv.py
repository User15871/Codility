# -*- coding: utf-8 -*-
"""
Created on Sat Jul 14 09:45:54 2018

@author: andy
"""

import math
def solution(A, B, K):
    # write your code in Python 3.6
    return(B//K-math.ceil(A/K)+1)
    pass
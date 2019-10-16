# -*- coding: utf-8 -*-
"""
Created on Tue Oct 15 22:58:17 2019

@author: Allan Santos
"""
import numpy as np

def stepFunction(soma):
    if( soma >= 1):
        return 1
    else: 
        return 0
    
def sigmoidFunction(soma):
    return 1 / (1  + np.exp(-soma))
    

def hyperbolicTanh(soma):
    return (np.exp(soma) - np.exp(-soma))  / ((np.exp(soma) + np.exp(-soma)))
    
result = stepFunction(-1)
print(result)

result2 = sigmoidFunction(-0.577)
print(result2)

result3 = hyperbolicTanh(-0.358)
print(result3)


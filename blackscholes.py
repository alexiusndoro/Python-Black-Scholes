# -*- coding: utf-8 -*-
"""
Created on Wed Dec 25 13:41:28 2019

@author: alexius
"""

#
import math
exp = math.exp 
import numpy as np
import scipy.stats as si
#import sympy as sy
#import sympy.statistics as systats

def European_call(S,K,r,sigma,T):
   #S spot price
   #K strike price
   #r risk free rate
   #sigma implied volatility
   #Maturity date
    
    
    d1 = (np.log(S/K)+(r + 0.5*np.square(sigma)*T))/sigma*np.sqrt(T)
    d2 = (np.log(S/K)+(r - 0.5*np.square(sigma)*T))/sigma*np.sqrt(T)
    
    call = S*si.norm.cdf(d1,0,1,) - K*pow(exp,-r*T)*si.norm.cdf(d2,0,1)
    
    return call

European_call(50, 100, 1, 0.05, 0.25)



    
    
    
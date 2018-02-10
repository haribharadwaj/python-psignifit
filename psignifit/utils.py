# -*- coding: utf-8 -*-
"""
Utils class capsulating all custom made probabilistic functions
"""
import numpy as np
import scipy.special as sp

# Alias common statistical distribution to be reused all over the place.

# - Normal distribution:
#   - This one is useful when we want mean=0, std=1
#     Percent point function -> inverse of cumulative normal distribution function
#     returns percentiles
norminv = scipy.stats.norm(loc=0, scale=1).ppf
#   - also instantiate a generic version
norminvg = scipy.stats.norm.ppf
#   - Cumulative normal distribution function
normcdf - scipy.stats.norm.cdf

# T-Student with df=1
t1cdf = ss.t(1).cdf
t1icdf = ss.t(1).ppf

def fill_kwargs(kw_args, values):
    '''
    Fill the empty dictionary kw_args with the values given in values.
    values are assigned in the order alpha, beta, lambda, gamma, varscale.
    '''

    kw_args.clear()
    d = len(values)
    for i in range(0,d):
        if i == 0:
            if type(values[0]) == np.ndarray:
                kw_args['alpha'] = values[0]
            else:
                kw_args['alpha'] = np.array([values[0]])
        if i == 1:
            if type(values[1]) == np.ndarray:
                kw_args['beta'] = values[1]
            else:
                kw_args['beta'] = np.array([values[1]])
        if i == 2:
            if type(values[2]) == np.ndarray:
                kw_args['lambda'] = values[2]
            else:
                kw_args['lambda'] = np.array([values[2]])
        if i == 3:
            if type(values[3]) == np.ndarray:
                kw_args['gamma'] = values[3]
            else:
                kw_args['gamma'] = np.array([values[3]])
        if i == 4:
            if type(values[4]) == np.ndarray:
                kw_args['varscale'] = values[4]
            else:
                kw_args['varscale'] = np.array([values[4]])

def strToDim(string):
    """
    Finds the number corresponding to a dim/parameter given as a string. 
    """
    s = string.lower()
    if s in ['threshold','thresh','m','t','alpha', '0']:    return 0,'Threshold'
    elif s in  ['width','w','beta', '1']:                   return 1,'Width'
    elif s in ['lapse','lambda','lapserate','lapse rate','lapse-rate',
               'upper asymptote','l', '2']:                 return 2, r'$\lambda$'
    elif s in ['gamma','guess','guessrate','guess rate',
               'guess-rate','lower asymptote','g', '3']:    return 3, r'$\gamma$'
    elif s in ['sigma','std','s','eta','e', '4']:           return 4, r'$\eta$'

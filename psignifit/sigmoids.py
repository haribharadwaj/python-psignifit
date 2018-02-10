import numpy as np
import scipy.stats
from .utils import norminv as _norminv
from .utils import norminvg as _norminvg

def gauss(X, m, width, PC=0.5, alpha=0.05):
    C = width/(_norminv(1-alpha) - _norminv(alpha))
    return my_normcdf(X, (m-_norminvg(PC, 0, C)), C)

def logistic(X, m, width, PC=0.5, alpha=0.05):
    return 1/(1 + np.exp(-2*np.log(1/alpha -1)/width*(X-m)+np.log(1/PC -1)))

def gumbel(X, m, width, PC=0.5, alpha=0.05):
    C = np.log(-np.log(alpha)) - np.log(-np.log(1-alpha))
    return 1 - np.exp(-np.exp(C/width*(X-m)+np.log(-np.log(1-PC))))

def rgumbel(X, m, width, PC=0.5, alpha=0.05):
    C = np.log(-np.log(1-alpha)) - np.log(-np.log(alpha))
    return np.exp(-np.exp(C/width*(X-m)+np.log(-np.log(PC))))

def logn(X, m, width, PC=0.5, alpha=0.05):
    return gauss(np.log(X), m, width, PC, alpha)

def weibull(X, m, width, PC=0.5, alpha=0.05):
    return gumbel(np.log(X), m, width, PC, alpha)

def tdist(X, m, width, PC=0.5, alpha=0.05):
    C = (my_t1icdf(1-alpha) - my_t1icdf(alpha))
    return my_t1cdf(C*(X-m)/width + my_t1icdf(PC))

def neg_gauss(X, m, width, PC=0.5, alpha=0.05):
    return 1 - gauss(X, m, width, 1-PC, alpha)

def neg_gumbel(X, m, width, PC=0.5, alpha=0.05):
    return 1 - gumbel(X, m, width, 1-PC, alpha)

def neg_rgumbel(X, m, width, PC=0.5, alpha=0.05):
    return 1 - rgumbel(X, m, width, 1-PC, alpha)

def neg_logn(X, m, width, PC=0.5, alpha=0.05):
    return 1 - logn(X, m, width, 1-PC, alpha)

def neg_weibull(X, m, width, PC=0.5, alpha=0.05):
    return 1 - weibull(X, m, width, 1-PC, alpha)

def neg_tdist(X, m, width, PC=0.5, alpha=0.05):
    return 1 - tdist(X, m, width, 1-PC, alpha)

# an alias for gauss
norm, neg_norm = gauss, neg_gauss
# aliases for tdist
student, neg_student = tdist, neg_tdist
heavytail, neg_heavytail = tdist, neg_tdist
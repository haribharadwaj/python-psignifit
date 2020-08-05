import numpy as _np

from .utils import normcdf as _normcdf
from .utils import norminv as _norminv
from .utils import norminvg as _norminvg
from .utils import t1cdf as _t1cdf
from .utils import t1icdf as _t1icdf

# sigmoid function = psi
# X -> stimulus levels (float)
# m -> threshold is the stimulus level at which the sigmoid has value PC (float)
#      psi(m) = PC , typically PC=0.5
# width -> the difference of stimulus levels where the sigmoid has value alpha and 1-alpha
#      width = X_(1-alpha) - X_(alpha)
#      psi(X_(1-alpha)) = 0.95 = 1-alpha
#      psi(X_(alpha)) = 0.05 = alpha

def gauss(X, m, width, PC=0.5, alpha=0.05):
    C = width / (_norminv(1 - alpha) - _norminv(alpha))
    return _normcdf(X, (m - _norminvg(PC, 0, C)), C)


def logistic(X, m, width, PC=0.5, alpha=0.05):
    return 1 / (1 + _np.exp(-2 * _np.log(1 / alpha - 1) / width *
                           (X - m) + _np.log(1 / PC - 1)))


def gumbel(X, m, width, PC=0.5, alpha=0.05):
    C = _np.log(-_np.log(alpha)) - _np.log(-_np.log(1 - alpha))
    return 1 - _np.exp(-_np.exp(C / width * (X - m) + _np.log(-_np.log(1 - PC))))


def rgumbel(X, m, width, PC=0.5, alpha=0.05):
    C = _np.log(-_np.log(1 - alpha)) - _np.log(-_np.log(alpha))
    return _np.exp(-_np.exp(C / width * (X - m) + _np.log(-_np.log(PC))))


def logn(X, m, width, PC=0.5, alpha=0.05):
    return gauss(_np.log(X), m, width, PC, alpha)


def weibull(X, m, width, PC=0.5, alpha=0.05):
    return gumbel(_np.log(X), m, width, PC, alpha)


def tdist(X, m, width, PC=0.5, alpha=0.05):
    C = (_t1icdf(1 - alpha) - _t1icdf(alpha))
    return _t1cdf(C * (X - m) / width + _t1icdf(PC))


def neg_gauss(X, m, width, PC=0.5, alpha=0.05):
    return 1 - gauss(X, m, width, 1 - PC, alpha)


def neg_gumbel(X, m, width, PC=0.5, alpha=0.05):
    return 1 - gumbel(X, m, width, 1 - PC, alpha)


def neg_rgumbel(X, m, width, PC=0.5, alpha=0.05):
    return 1 - rgumbel(X, m, width, 1 - PC, alpha)


def neg_logn(X, m, width, PC=0.5, alpha=0.05):
    return 1 - logn(X, m, width, 1 - PC, alpha)


def neg_weibull(X, m, width, PC=0.5, alpha=0.05):
    return 1 - weibull(X, m, width, 1 - PC, alpha)


def neg_tdist(X, m, width, PC=0.5, alpha=0.05):
    return 1 - tdist(X, m, width, 1 - PC, alpha)


# an alias for gauss
norm, neg_norm = gauss, neg_gauss
# aliases for tdist
student, neg_student = tdist, neg_tdist
heavytail, neg_heavytail = tdist, neg_tdist
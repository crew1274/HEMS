from __future__ import division
import numpy as np
import math as m
import scipy.sparse as sp
import scipy.sparse.linalg as spln
import scipy.stats as sts


def multivariate_gaussian_pdf(x, loc_v, covm):
    assert(loc_v.shape[0]>loc_v.shape[1]), 'loc_v must be a row vector'
    assert(x.shape[0]> x.shape[1]), 'x must be a row vector'
    assert(covm.shape[0]==covm.shape[1]), 'cov_matrix must be square'
    assert(loc_v.shape[0]==covm.shape[0]), 'cov_matrix and the loc_v must have the same dimensions'
    assert(x.shape[0]==covm.shape[0]), 'cov_matrix and x must have the same dimensions'
    
    normal_coeff = 1./(  ((2.*np.pi)**(len(loc_v)/2.)) * (np.linalg.det(covm)**(0.5)) )
    func = np.exp((0.5) * ((x-loc_v).T.dot(np.linalg.inv(covm))).dot((x-loc_v)))
    
    return float(normal_coeff*func)


def lognorm_pdf(x, loc_v, covm):
    nx = len(covm)
    normal_coeff = nx * m.log(2*m.pi) + np.linalg.slogdet(covm)[1]
    err = (x-loc_v)
    if (sp.issparse(covm)):
        numerator = spln.spsolve(covm, err).T.dot(err)
    else:
        numerator = np.linalg.solve(covm,err).T.dot(err)
    #return float(-0.5*(normal_coeff + numerator))
    return np.exp(float(-0.5*(normal_coeff + numerator)))



x = np.array([[0],[0]])
mu  = np.array([[0],[0]])
cov = np.eye(2)
print(x)
print(mu)
print(cov)
print (multivariate_gaussian_pdf(x, mu, cov))
print (sts.multivariate_normal(np.concatenate(mu), cov).pdf(np.concatenate(x)))
print (lognorm_pdf(x, mu, cov))
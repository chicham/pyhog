cimport numpy as np
import numpy as np
from libcpp.vector cimport vector
from libcpp.memory cimport shared_ptr


cdef extern from "pyhog_impl.hpp":
    cdef cppclass FeatureVector:
        FeatureVector();
        FeatureVector(vector[double], int, int, int);
        vector[double] data
        int rows
        int cols
        int size
    cdef FeatureVector process(double*, int, int, int, int)


cpdef np.ndarray[np.float, ndim=3] hog_feature(double[:, :, :] im, int sbin=4):
    shape = im.shape
    cdef double[:, :, :] im_f = im.copy_fortran()
    cdef FeatureVector feat = process(<double*>&im_f[0,0,0], shape[0], shape[1], shape[2], sbin)
    cdef double[:, :, :] out = <double[:feat.rows:1, :feat.cols, :feat.size]>feat.data.data()
    return np.asarray(out.copy())

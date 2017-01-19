cimport numpy as np
import numpy as np
from libcpp.vector cimport vector
from libcpp.memory cimport shared_ptr


cdef extern from "../cpp/hog.hpp":
    cdef cppclass FeatureVector:
        FeatureVector();
        FeatureVector(vector[double], int, int, int);
        vector[double] data
        int rows
        int cols
        int size
    cdef FeatureVector process(double*, int, int, int, int) nogil
    cpdef int hog_size(int, int)


cpdef np.ndarray[np.float, ndim=3] hog(double[:, :, :] im, int sbin=4):
    cdef int rows = im.shape[0]
    cdef int cols = im.shape[1]
    cdef int size = im.shape[2]
    cdef double[:, :, :] im_f = im.copy_fortran()
    cdef FeatureVector feat = process(<double*>&im_f[0,0,0], rows, cols, size, sbin)
    cdef double[:, :, :] out = <double[:feat.rows:1, :feat.cols, :feat.size]>feat.data.data()
    return np.asarray(out.copy())

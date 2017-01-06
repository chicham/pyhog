from setuptools import setup, find_packages, Extension
from Cython.Build import cythonize
import numpy as np

extensions = [
    # Extension('pyhog.features_pedro_py',
    #           extra_compile_args=['-O2', '-ffast-math',
    #                               '-msse2', '-DNUMPYCHECK',
    #                               '-DNDEBUG', '-fPIC'],
    #           sources=['./pyhog/features_pedro_py.cc']
    #           ),
    Extension("pyhog.pyhog",
              sources=["./pyhog/pyhog.pyx", "./pyhog/pyhog_impl.cpp"],
              extra_compile_args=['-std=c++14', '-fopenmp'],
              language='c++')
              ]

setup(name='pyhog',
      version='1.1',
      author='hicham randrianarivo',
      packages=find_packages(),
      ext_modules=cythonize(extensions),
      include_dirs=[np.get_include()])


def build():
    """
    Build the library by compiling first the CPP extension then compile the cython binding
    :return:
    """
    pass

from setuptools import setup, find_packages, Extension
from Cython.Build import cythonize
import numpy as np

extensions = [
    Extension("pyhog.feature",
              sources=["./pyhog/feature.pyx", "./cpp/hog.cpp"],
              extra_compile_args=['-std=c++14', '-fopenmp'],
              language='c++')
]

setup(name='pyhog',
      version='1.1',
      author='hicham randrianarivo',
      packages=find_packages(),
      ext_modules=cythonize(extensions),
      include_dirs=[np.get_include()])

from setuptools import setup, find_packages, Extension
import numpy as np

setup(name='pyhog',
      version='0.1a0',
      author='Daniel Maturana',
      packages=find_packages(),
      ext_modules=[Extension('pyhog.features_pedro_py',
                             extra_compile_args=['-O2', '-ffast-math',
                                                 '-msse2', '-DNUMPYCHECK',
                                                 '-DNDEBUG', '-fPIC'],
                             sources=['./pyhog/features_pedro_py.cc'])],
      include_dirs=[np.get_include()])

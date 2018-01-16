#!/usr/bin/env python
from __future__ import unicode_literals
"""
Copyright (c) 2017 Massachusetts Institute of Technology (MIT)
All rights reserved.
Distributed under the terms of the BSD 3-clause license.
The full license is in the LICENSE file, distributed with this software.
"""

"""Setup file for the digital_rf package."""

INSTALL_REQUIRES=['h5py', 'numpy']

from setuptools import setup, Extension, find_packages
from setuptools.command.build_py import build_py
import os
import numpy



# Get the long description from the README file
long_description = open('README.rst').read()

setup(
    name='digital_rf',
    version='2.0',
    description='Python tools to read and write Digital RF data in HDF5 format',
    long_description=long_description,

    # url='http://www.haystack.mit.edu/digital_rf/',

    author='MIT Haystack Observatory',
    # author_email='digital_rf@haystack.mit.edu',

    license='BSD-3-Clause',

    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Console',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: BSD License',
        'Programming Language :: Python',
        'Topic :: Scientific/Engineering',
    ],

    keywords='hdf5 radio rf',

    install_requires=INSTALL_REQUIRES,
    extras_require={
        'watchdog': ['watchdog'],
    },

    package_dir={
        'digital_rf': 'python',
    },
    packages=['digital_rf'],
    entry_points= {
        'console_scripts': ['drf=digital_rf.drf_command:main'],
    },
    scripts=[
        'tools/digital_metadata_archive.py',
        'tools/digital_rf_archive.py',
        'tools/digital_rf_upconvert.py',
        'tools/drf_cross_sti.py',
        'tools/drf_plot.py',
        'tools/drf_sti.py',
        'tools/drf_sound.py',
        'tools/verify_digital_rf_upconvert.py',
    ],
)

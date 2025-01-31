#!/usr/bin/env python
# Copyright (c) 2017 pandas-gbq Authors All rights reserved.
# Use of this source code is governed by a BSD-style
# license that can be found in the LICENSE file.

# -*- coding: utf-8 -*-

import versioneer
from setuptools import find_packages, setup

NAME = "pandas-gbq"


# versioning
cmdclass = versioneer.get_cmdclass()


def readme():
    with open("README.rst") as f:
        return f.read()


INSTALL_REQUIRES = [
    "setuptools",
    "pandas>=0.23.2",
    "pydata-google-auth",
    "google-auth",
    "google-auth-oauthlib",
    # 2.4.* has a bug where waiting for the query can hang indefinitely.
    # https://github.com/pydata/pandas-gbq/issues/343
    "google-cloud-bigquery[bqstorage,pandas]>=1.11.1,<3.0.0dev,!=2.4.*",
]

extras = {"tqdm": "tqdm>=4.23.0"}

setup(
    name=NAME,
    version=versioneer.get_version(),
    cmdclass=versioneer.get_cmdclass(),
    description="Pandas interface to Google BigQuery",
    long_description=readme(),
    license="BSD License",
    author="The PyData Development Team",
    author_email="pydata@googlegroups.com",
    url="https://github.com/pydata/pandas-gbq",
    classifiers=[
        "Development Status :: 4 - Beta",
        "Environment :: Console",
        "Intended Audience :: Science/Research",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Topic :: Scientific/Engineering",
    ],
    keywords="data",
    install_requires=INSTALL_REQUIRES,
    extras_require=extras,
    python_requires=">=3.7",
    packages=find_packages(exclude=["contrib", "docs", "tests*"]),
    test_suite="tests",
)

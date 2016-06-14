#!/usr/bin/env python
# coding=utf-8

import os
from distutils.core import setup

delattr(os, 'link')

setup(
    name='hut',
    version='1.0',
    author='Jerome Belleman',
    author_email='Jerome.Belleman@gmail.com',
    url='http://cern.ch/jbl',
    description="A Kibana dashboard template tool",
    long_description="Hut generates Kibana dashboard JSON files from Mako templates. It makes it possible to programmatically, and with less JSON code, write large numbers of complex dashboards.",
    scripts=['hut'],
    py_modules=['twigs'],
    data_files=[('share/man/man1', ['inkgrad.1'])],
)

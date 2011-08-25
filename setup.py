# -*- coding: utf-8 -*-
__author__ = 'joaoalf'

from setuptools import setup

setup(
    name = u'PySPED',
    description = u'Sistema Público de Escrituração Digital em Python',
    author = u'Aristides Caldeira',
    author_email = u'aristides.caldeira@taugars.com.br',
    packages = ['pysped'],
    include_package_data=True,
    install_requires=['setuptools',
                      'lxml',
                      'suds',
                      'PyOpenSSL',
                      'PyXMLSec',
                      'reportlab',
                      'Geraldo'],
)
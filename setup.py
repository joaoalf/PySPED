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
    zip_safe = False,
    dependency_links = ['https://github.com/joaoalf/geraldo/tarball/master#egg=Geraldo-0.1dev_joaoalf_branch'],
    install_requires=['setuptools',
                      'lxml',
                      'suds',
                      'PyOpenSSL',
                      'PyXMLSec',
                      'Geraldo==0.1dev_joaoalf_branch'],
)
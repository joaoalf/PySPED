# -*- coding: utf-8 -*-

import os
from setuptools import setup, find_packages

setup(
    name = u'PySPED',
    version = '0.1dev_joaoalf_branch',
    description = u'Sistema Público de Escrituração Digital em Python',
    author = u'Aristides Caldeira',
    author_email = u'aristides.caldeira@taugars.com.br',
    packages = find_packages(),
    package_data = {'pysped.nfe.manual_401': [os.path.join('schema', 'pl_006g', '*')],
                    'pysped.nfe.danfe': [os.path.join('fonts', '*')],
                    'pysped.relato_sped': [os.path.join('fonts', '*')],
                    'pysped.xml_sped': [os.path.join('schema', '*'),
                                        os.path.join('cadeia-certificadora', '*'),
                                        os.path.join('cadeia-certificadora', 'certificados', '*')]},
    include_package_data=True,
    zip_safe = False,
    dependency_links = ['https://github.com/joaoalf/geraldo/tarball/master#egg=Geraldo-0.4dev_joaoalf_branch'],
    install_requires=['setuptools',
                      'lxml',
                      'suds',
                      'PyOpenSSL==0.12',
                      'PyXMLSec',
                      'Geraldo==0.4dev_joaoalf_branch'],
)
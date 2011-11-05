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
    package_data = {'pysped.nfe.manual_401': [os.path.join(u'schema', u'pl_006g', u'*')],
                    'pysped.nfe.danfe': [os.path.join(u'fonts', u'*')],
                    'pysped.relato_sped': [os.path.join(u'fonts', u'*')],
                    'pysped.xml_sped': [os.path.join(u'schema', u'*'),
                                        os.path.join(u'cadeia-certificadora', u'README'),
                                        os.path.join(u'cadeia-certificadora', u'*.*'),
                                        os.path.join(u'cadeia-certificadora', u'certificados', u'*')]},
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
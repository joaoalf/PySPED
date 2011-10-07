# -*- coding: utf-8 -*-
__author__ = 'joaoalf'

from setuptools import setup, find_packages

setup(
    name = u'PySPED',
    description = u'Sistema Público de Escrituração Digital em Python',
    author = u'Aristides Caldeira',
    author_email = u'aristides.caldeira@taugars.com.br',
    packages = ['pysped',
                'pysped.nfe',
                'pysped.nfe.danfe',
                'pysped.nfe.manual_300',
                'pysped.nfe.manual_401',
                'pysped.nfe.manual_401.schema',
                'pysped.nfe.manual_401.schema.pl_006g',
                'pysped.xml_sped',
                'pysped.relato_sped'],
    include_package_data=True,
    zip_safe = False,
    dependency_links = ['https://github.com/joaoalf/geraldo/tarball/master#egg=Geraldo-0.1dev_joaoalf_branch'],
    install_requires=['setuptools',
                      'lxml',
                      'suds',
                      'PyOpenSSL==0.12',
                      'PyXMLSec',
                      'Geraldo==0.1dev_joaoalf_branch'],
)
# -*- coding: utf-8 -*-

from pysped.nfe import ProcessadorNFe
from pysped.nfe.webservices_flags import *
from os.path import abspath, dirname

FILE_DIR = abspath(dirname(__file__))

if __name__ == '__main__':
    p = ProcessadorNFe()
    p.versao              = u'2.00'
    p.estado              = u'SP'
    # arquivo 'certificado_caminho.txt' deve conter o caminho para o 'certificado.pfx'
    p.certificado.arquivo = open(FILE_DIR+'/certificado_caminho.txt').read().strip()
    # arquivo 'certificado_senha.txt' deve conter a senha para o 'certificado.pfx'
    p.certificado.senha   = open(FILE_DIR+'/certificado_senha.txt').read().strip()
    p.salvar_arquivos      = True
    p.contingencia_SCAN   = False
    p.caminho = u'' 

    #
    # O retorno de cada webservice é um dicionário
    # estruturado da seguinte maneira:
    # { TIPO_DO_WS_EXECUTADO: {
    #       u'envio'   : InstanciaDaMensagemDeEnvio,
    #       u'resposta': InstanciaDaMensagemDeResposta,
    #       }
    # }
    #
    processo = p.consultar_servico()
    
    print processo.envio.xml
    print
    print processo.resposta.xml
    print
    print processo.resposta.reason


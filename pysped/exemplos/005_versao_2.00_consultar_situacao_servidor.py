# -*- coding: utf-8 -*-

from pysped.nfe import ProcessadorNFe
from pysped.nfe.webservices_flags import *


if __name__ == '__main__':
    p = ProcessadorNFe()
    p.versao              = u'2.00'
    p.estado              = u'SP'
    # arquivo 'certificado_caminho.txt' deve conter o caminho para o 'certificado.pfx'
    p.certificado.arquivo = open('certificado_caminho.txt').read().strip()
    # arquivo 'certificado_senha.txt' deve conter a senha para o 'certificado.pfx'
    p.certificado.senha   = open('certificado_senha.txt').read().strip()
    p.salva_arquivos      = True
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
    
    print processo[WS_NFE_SITUACAO][u'envio'].xml
    print
    print processo[WS_NFE_SITUACAO][u'resposta'].xml
    

import certLib as CERT

def criaCA():
    print('Essas ações são feitas pela Autoridade Certificado')
    priCA, priCA_pem = CERT.geraChavePrivada(2048, 'caPrivada.pem')
    pubCA, pubCA_pem = CERT.geraChavePublica(priCA, 'caPublica.pem')

    # CN='PUCPR.br', O='Politecnica PUCPR', C='BR', S='Parana', L='Curitiba'
    dn = {'cn' : 'PUCPR.br', 'o':'Politecnica PUCPR', 'c':'BR', 's':'Parana', 'l':'Curitiba'}
    certCA = CERT.geraAutoAssinado(priCA, pubCA, dn, 'certCA.pem') 
    certCA = CERT.carregaCertificado("certCA.pem", show=True)
    

def geraCSR():
    print('Essas ações são feitas pela administrador do Servidor Web')
    priEU, priEU_pem = CERT.geraChavePrivada(2048, 'euPrivada.pem')
    pubEU, pubEU_pem = CERT.geraChavePublica(priEU, 'euPublica.pem')


    # CN='bcc.pucpr.br', O='Ciencia da Computacao', C='BR', S='Parana', L='Curitiba'
    dn = {'cn' : 'bcc.pucpr.br', 'o':'Ciencia da Computacao', 'c':'BR', 's':'Parana', 'l':'Curitiba'} 
    csr_pem =  CERT.geraCSR(priEU, dn, 'csr.pem')
    csr = CERT.carregaCSR('csr.pem', show=True) 
    
def assinaCSR():
    print('Essas ações são feitas pela CA')
    csr = CERT.carregaCSR('csr.pem', show=True) 
    certCA = CERT.carregaCertificado("certCA.pem", show=True)
    priCA = CERT.carregaChavePrivada('caPrivada.pem')

    certEU = CERT.assinaCSR(csr, certCA, priCA, 'certEU.pem')
    certEU = CERT.carregaCertificado('certEU.pem', show=True)
    
def validaCertificado():
    print('Essas ações são feitas pelo navegador Web')
    certEU = CERT.carregaCertificado('certEU.pem', show=False)
    certCA = CERT.carregaCertificado("certCA.pem", show=False)
    print( CERT.verificaCertificado(certEU, certCA) )
    

#--------------------------------------------------------------

# 1) Crie uma CA com a seguinte DN
# CN='PUCPR.br', O='Politecnica PUCPR', C='BR', S='Parana', L='Curitiba'
criaCA()

# 2) Crie um CSR para o servidor Web e assine com a CA
# CN='bcc.pucpr.br', O='Ciencia da Computacao', C='BR', S='Parana', L='Curitiba'
geraCSR()
assinaCSR()

# 3) Faça a verificação do Certificado pelo navegador Web
validaCertificado()


"""
PERGUNTAS:

1) Como o certificado da CA é validado?
2) Qual chave a CA usa para assinar o CSR do Servidor Web?
3) O certificado do servidor contém a chave privada do Servidor Web?
4) Quais informações o browser precisa conhecer para validar o certificado do Servidor Web?
"""



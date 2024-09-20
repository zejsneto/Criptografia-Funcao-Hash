import hashlib

# Função para calcular o hash SHA256 e MD5
def calcular_hashs(frase):
    sha256_hash = hashlib.sha256(frase.encode('utf-8')).hexdigest()
    md5_hash = hashlib.md5(frase.encode('utf-8')).hexdigest()
    return sha256_hash, md5_hash

# Lista de frases fornecidas
frases = [
    "A primeira das instituições criadas pelo Pe. Roberto Sabóia de Medeiros foi a antiga Escola Superior de Administração de Negócios de São Paulo - ESAN/SP.",
    "A FEI é uma instituição vinculada estatutariamente à Companhia de Jesus",
    "Em 20 de janeiro de 1951 foi realizada a sessão solene da congregação para a Colação de Grau da primeira turma da Faculdade de Engenharia Industrial.",
    "A Capela Santo Inácio de Loyola foi construída no ano de 1978, em concreto aparente.",
    "Tendo como função principal a promoção do aprimoramento profissional no campo administrativo e tecnológico, o IECAT (Instituto de Especialização em Ciências Administrativas e Tecnológicas) foi criado em 1982",
    "Dentro de uma proposta de integração e de agregação de competências, visando a excelência de seus cursos, as instituições FEI, FCI e ESAN foram transformadas no Centro Universitário da FEI no ano de 2002.",
    "O Centro Universitário da FEI passou a fazer parte do seleto grupo que produz ciência no Brasil, quando a CAPES aprovou o primeiro curso de Mestrado em Engenharia Elétrica em 2005.",
    "Em 2016 foi realizada a primeira edição do congresso de inovação - Megatendências 2050.",
    "Em 2012 o Centro Universitário FEI celebrou 70 anos de história e de excelência na inovação e na formação de mais de 50 mil profissionais altamente qualificados para o setor empresarial, entre Administradores, Engenheiros e Cientistas da Computação.",
    "Em 1999 iniciam-se as atividades da FCI (Faculdade de Informática), como o curso de Ciência da Computação."
]

# Hashes fornecidos para verificação (SHA256 e o MD5)
hashes_fornecidos = [
    ("d24de3ec3835115c576a55188a31761b73af93ed2c45a171c810bb66b24b08f9", "c850e1a34a6ed572e0758ccd9c615bda"),
    ("6979a3d7a19e5921ae00ca7db9b814e1b83831dcedfca33dbb72e761ca084337", "b710771da8d7521524f45233ea9dd9e1"),
    ("6c582a993ba3ea454f11221a374878e534cfe666060c87ba03127de07f1ca4e6", "55748c2cb669a9d9508677cb914cb025"),
    ("254e695d0f8835651bc231f9cf1b2a7a097b849648f05f79f1855a55f85b089e", "f4a8a299fd4da2a5d70b374be2e48147"),
    ("d2150d688c337fc57e235adafd57f86d7aba0b8682c249b1006ba592706f88a0", "1c4ecc238571333ae507f82ff6a5e9e4"),
    ("faefb927a21dd282ee00effe42bc0688f649450677a61edce15863a15461b721", "98420532cbf1be32a98be579f592cd72"),
    ("da9f214449005850f4fd552238658820434c15ca06389d018b1814bb376abaa6", "2e20bfbece6fdc62de4c4bb80a77ba1f"),
    ("56f4ba0ea34d91fe386f09dc687f1c35c757009b0230a828fa43e48ac08f8d0c", "5cbf7c58bf9acd451c3bf1b48392a9e6"),
    ("2707325bd4929bbbadb422851a2248615bf7998bf3607b6ad934168be6a45859", "a0a80cbc42bcd7b4b6ab317d0d2efa33"),
    ("b2ff0457c8c20ccd84e20cd72f06c08140b8ea472d6a6848a5c291319bf9e4a8", "0288b32001adf2f237ba8410f8415e50")
]

# Tabela de verificação
tabela_verificacao = []

for i, frase in enumerate(frases):
    sha256_hash, md5_hash = calcular_hashs(frase)
    sha256_fornecido, md5_fornecido = hashes_fornecidos[i]
    sha256_verificado = sha256_hash == sha256_fornecido
    md5_verificado = md5_hash == md5_fornecido
    
    # Cenários possíveis
    if sha256_verificado and md5_verificado:
        resultado = "SHA256 e MD5 corretos"
    elif sha256_verificado:
        resultado = "Somente SHA256 correto"
    elif md5_verificado:
        resultado = "Somente MD5 correto"
    else:
        resultado = "Nenhum dos dois corretos"
    
    # Adiciona resultado na tabeal
    tabela_verificacao.append((frase, resultado))

i = 1

# Exibindo os resultados
for frase, resultado in tabela_verificacao:
    print(f'Frase {i}: "{frase}"\nResultado: {resultado}\n')
    i += 1
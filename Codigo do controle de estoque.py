# ------------------------- FUNÇOES --------------------------
# Função para Cadastro de peças
def cadastrarPeca(codigo):
    print('\nVocê selecionou a opção CADASTRAR PEÇAS\n' +
          'Por favor, preencha os dados abaixo')
    print('Código da Peça: {}'.format(codigo))
    nome = input('Digite o NOME da peça: ')
    fabricante = input('Digite o FABRICANTE da peça: ')
    valor = float(input('Digite o VALOR (R$) da peça: '))
    # armazenando os dados inseridos pelo usuario em um dicionário
    dici_peca = {'codigo': codigo,
                 'nome': nome,
                 'fabricante': fabricante,
                 'valor': valor}
    # copiando o dicionário para a lista global de peças
    lista_pecas.append(dici_peca.copy())

# Função para Consulta de peças


def consultarPeca():
    print('\nVocê selecionou a opção CONSULTAR PEÇAS')
    # laço de repetição
    while True:
        consulta = input('\nEscolha uma ação desejada:\n' +
                         '1 - Consultar Todas as Peças\n' +
                         '2 - Consultar Peças por Código\n' +
                         '3 - Consultar Peças por Fabricante\n' +
                         '4 - Retornar\n' +
                         '>> ')
        if (consulta == '1'):
            print('Todas as Peças:')
            for peca in lista_pecas:  # peca irá varrer a lista de peças criada
                print('-'*40)
                for key, value in peca.items():  # varredura das chaves e valores do dicionário peca
                    print("{}: {}". format(key, value))
        elif (consulta == '2'):
            print('Peças por Código:')
            codigo_desejado = int(input('Digite o CÓDIGO da Peça: '))
            for peca in lista_pecas:
                # caso a varredura no dicionário peca encontre um código igual ao desejado
                if (peca['codigo'] == codigo_desejado):
                    print('-'*40)
                    for key, value in peca.items():
                        print("{}: {}". format(key, value))
        elif (consulta == '3'):
            print('Peças por Fabricante:')
            fabricante_desejado = input('Digite o FABRICANTE da Peça: ')
            for peca in lista_pecas:
                # caso a varredura no dicionário peca encontre um fabricante igual ao desejado
                if (peca['fabricante'] == fabricante_desejado):
                    print('-'*40)
                    for key, value in peca.items():
                        print("{}: {}". format(key, value))
        elif (consulta == '4'):
            return  # sai da função consultar e volta para o programa principal
        else:
            print('Opção inválida. Digite um número de 1 a 4.')
            continue  # volta para o início do laço

# Função para Remover peças


def removerPeca():
    print('\nVocê selecionou a opção REMOVER PEÇAS')
    codigo_desejado = int(input('Digite o CÓDIGO da Peça: '))
    for peca in lista_pecas:
        if (peca['codigo'] == codigo_desejado):
            # removendo a peça da lista com a função remove
            lista_pecas.remove(peca)
            print('Peça removida com sucesso!')


# -------------------- PROGRAMA PRINCIPAL --------------------
# variáveis globais
lista_pecas = []
codigo_peca = 0
print('\nBem-vindo ao Controle de Estoque da Bicicletaria da Isabel Ribeiro Barbosa')
# laço de repetição
while True:
    acao_desejada = input('\nEscolha uma ação desejada:\n' +
                          '1 - Cadastrar Peça\n' +
                          '2 - Consultar Peça\n' +
                          '3 - Remover Peça\n' +
                          '4 - Sair\n' +
                          '>> ')
    if (acao_desejada == '1'):
        codigo_peca += 1
        cadastrarPeca(codigo_peca)
    elif (acao_desejada == '2'):
        consultarPeca()
    elif (acao_desejada == '3'):
        removerPeca()
    elif (acao_desejada == '4'):
        break  # encerra o programa
    else:
        print('Opção inválida. Digite um número de 1 a 4.')
        continue  # volta para o início do laço

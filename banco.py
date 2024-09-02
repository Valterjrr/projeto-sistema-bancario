# sistema bancario com operações de saque, depósito e visualisar extrato

# Para o DEPOSITO:

# deve ser possível depositar apenas valores positivos para a conta / done
# todos os depósitos devem ser armasenados em uma variavel e exibidos na operaçao extrato / doing


# Para o saque:
# o sistema só permite 3 saques diarios com limite de 500 por saque / done
# se n tiver saldo em conta, o sistema deve informar isso / done
# todos os saques devem esta numa variavel e exibidos na operaçao extrato / doing


# Para o Extrato:
# lista todas as operações feitas. No fim, deve informar o saldo atual da conta no formato R$ xx.xx

#aprendisados:
#   1. se nao praticar, vai esquecer
#   2. documente o código desde o início, isso evita que vc volte no outro dia e demore mt revisando a lógica e entendendo o código
#   3. 
#
#
#
#
#
#


def deposito(saldo,caracteristicas_transaçao,historico):
    quantia = float(input('Digite a quantia que você deseja depositar: '))

    if quantia > 0:
        saldo += quantia
        print(f'''Seu depósito foi realisado com sucesso.
              Seu saldo atual: R$ {saldo:.2f}\n\n\n''')
        caracteristicas_transaçao['tipo de operaçao'] = 'Deposito'
        caracteristicas_transaçao['quantia'] = quantia
        historico.append(caracteristicas_transaçao)
        return saldo
        
    elif quantia <= 0:
        print(f'Desculpe, nao é possível depositar essa quantia.\n')


def saque(saldo,quantidade_saques,caracteristicas_transaçao,historico):
    if saldo == 0:
        print(f'Desculpe, seu saldo atual nao permite faser essa transaçao.\n\n')

    elif saldo > 0:
        if quantidade_saques == 3:
            print(f'Desculpe, voce ja atingiu o limite de saques diarios.\n\n')

        elif quantidade_saques < 3:
            quantia = float(input(f'Digite a quantia que você deseja faser o saque: \n'))

            if quantia > saldo:
                print(f'''Desculpe, nao é possível faser o saque.
                      a quantia solicitada é maior que o disponível em sua conta.\n\n''')
                
            else:
                if quantia > 500:
                    print(f'Desculpe, a quantia solicitada ultrapassa o limite de saque.\n\n')
                else:
                    saldo -= quantia
                    print(f'''Operaçao realisada com sucesso.
                        Seu saldo atual: R$ {saldo:.2f}\n\n''' )
                    caracteristicas_transaçao['tipo de operaçao'] = 'saque'
                    caracteristicas_transaçao['quantia'] = quantia

                    historico.append(caracteristicas_transaçao)
    return saldo

def extrato(saldo,lista):
    print(f'aqui esta o seu histórico de transações: \n')

    chaves_dicionario = ['tipo de operaçao','quantia']

    for ordem_de_transações in range(0,len(lista)):
        print(f'{chaves_dicionario[0]} : {lista[ordem_de_transações][chaves_dicionario[0]]}')
        print(f'{chaves_dicionario[1]} : {lista[ordem_de_transações][chaves_dicionario[1]]}\n')

    print(f'Seu saldo atual é: {saldo:.2f}')
    print(f'\n\n')


saldo_atual = 0
historico_transações = []
saques = 0


is_running = True

while is_running:
    detalhes_operaçao = {} # os dados da operaçao sao guardados na lista, o dicionario so guarda temporiariamente.
    operaçao = input(f'''ola SR. valter!
        qual operaçao deseja realisar:
        deposito [D]
        saque    [S]
        extrato  [E]
        Sair     [Q]
        
        Operaçao:  ''')
    operaçao = operaçao.upper()

    if operaçao == 'D':
        saldo_atual = deposito(saldo=saldo_atual, caracteristicas_transaçao = detalhes_operaçao, historico= historico_transações )

    elif operaçao == 'S':
        saldo_atual = saque(saldo=saldo_atual, quantidade_saques=saques, caracteristicas_transaçao=detalhes_operaçao, historico=historico_transações)
        saques += 1

    elif operaçao == 'E':
        extrato(saldo_atual, historico_transações)
        

    elif operaçao == 'Q':
        print(f'Tenha um bom dia!')
        is_running = False
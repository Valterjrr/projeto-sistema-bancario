# sistema bancário com operações de saque, depósito e visualizar extrato

# Para o DEPOSITO:

# deve ser possível depositar apenas valores positivos para a conta.
# todos os depósitos devem ser armasenados em uma variavel e exibidos na operaçao extrato.


# Para o SAQUE:

# o sistema só permite 3 saques diarios com limite de 500 por saque.
# se não tiver saldo em conta, o sistema deve informar.
# todos os saques devem estar numa variavel e exibidos na operaçao extrato.


# Para o EXTRATO:
# lista todas as operações feitas. No fim, deve informar o saldo atual da conta no formato R$ xx.xx




def deposito(saldo,caracteristicas_transaçao,historico):
    quantia = float(input('Digite a quantia que você deseja depositar: '))

    if quantia > 0:
        saldo += quantia
        print(f'''Seu depósito foi realizado com sucesso.
Seu saldo atual: R$ {saldo:.2f}\n\n''')
        
        caracteristicas_transaçao['tipo de operaçao'] = 'Deposito'
        caracteristicas_transaçao['quantia'] = quantia
        historico.append(caracteristicas_transaçao)
        return saldo
        
    elif quantia <= 0:
        print(f'Desculpe, nao é possível depositar essa quantia.\n\n')


def saque(saldo,caracteristicas_transaçao,historico):
    if saldo == 0:
        print(f'Desculpe, seu saldo atual nao permite fazer essa transaçao.\n\n')

    elif saldo > 0:
        quantia = float(input(f'Digite a quantia que você deseja fazer o saque: '))

        if quantia > saldo:
            print(f'''Desculpe, nao é possível fazer o saque.
A quantia solicitada é maior que o disponível em sua conta.\n\n''')
                
        else:
            if quantia > 500:
                print(f'Desculpe, a quantia solicitada ultrapassa o limite de saque.\n\n')
            else:
                saldo -= quantia
                print(f'''Operaçao realizada com sucesso.
Seu saldo atual: R$ {saldo:.2f}\n\n''' )
                    
                caracteristicas_transaçao['tipo de operaçao'] = 'saque'
                caracteristicas_transaçao['quantia'] = quantia

                historico.append(caracteristicas_transaçao)
    return saldo

def extrato(saldo,lista):
    print(f'Aqui esta o seu histórico de transações: \n')

    chaves_dicionario = ['tipo de operaçao','quantia']

    for ordem_de_transações in range(0,len(lista)):
        print(f'{chaves_dicionario[0]} : {lista[ordem_de_transações][chaves_dicionario[0]]}')
        print(f'{chaves_dicionario[1]} : {lista[ordem_de_transações][chaves_dicionario[1]]}\n')

    print(f'Seu saldo atual: {saldo:.2f}')
    print(f'\n\n')


saldo_atual = 0
historico_transações = []
saques = 0


is_running = True

while is_running:
    detalhes_operaçao = {} # os dados da operação são guardados na lista, o dicionário apenas guarda temporiariamente.
    operaçao = input(f'''Olá, Sr. Valter!
        qual operaçao deseja realizar:
        deposito [D]
        saque    [S]
        extrato  [E]
        Sair     [Q]
        
        Operaçao:  ''')
    operaçao = operaçao.upper()

    if operaçao == 'D':
        saldo_atual = deposito(saldo=saldo_atual, caracteristicas_transaçao = detalhes_operaçao, historico= historico_transações )

    elif operaçao == 'S':
        if saques < 3:
            check_saldo = saldo_atual
            saldo_atual = saque(saldo=saldo_atual, caracteristicas_transaçao=detalhes_operaçao, historico=historico_transações)

            if check_saldo != saldo_atual: # Se a função for chamada, mas não for possível sacar, check_saldo vai ser igual a saldo_atual. Logo não houve saque.
                saques += 1
        
        elif saques == 3:
            print(f'Desculpe, voce ja atingiu o limite de saques diarios.\n\n')

    elif operaçao == 'E':
        extrato(saldo_atual, historico_transações)
        

    elif operaçao == 'Q':
        print(f'Tenha um bom dia!')
        is_running = False

    else:
        print(f'Operaçao invalida.\n')
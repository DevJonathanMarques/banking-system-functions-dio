
#MENUS
menu_usuarios = """

[0] Criar usuário
[1] Acessar usuário
[2] Sair do sistema

=> """

menu_conta = """

[0] Criar conta
[1] Acessar conta
[2] Sair do usuário

=> """

menu_actions = """

[0] Depositar
[1] Sacar
[2] Extrato
[3] Sair da conta

=> """

#USUÁRIOS
def criar_usuario(usuarios, contas):
    cpf = input('Insira seu CPF =>')

    if usuarios.get(cpf) == None:
        usuarios[cpf] = dict()

        nome = input('Insira seu nome =>')
        data_de_nascimento = input('Insira sua data de nascimento =>')
        endereço = input('Insira seu endereço no formato *logradouro, número - bairro - cidade / sigla estado* =>')
        
        usuarios[cpf]['nome'] = nome
        usuarios[cpf]['data_de_nascimento'] = data_de_nascimento
        usuarios[cpf]['endereço'] = endereço

        contas[cpf] = dict()

        return "Usuário criado com sucesso"
    else:
        return "Já existe um usuário com esse CPF!"

def acessar_usuario(usuarios):
    cpf = input('Insira seu CPF =>')

    if usuarios.get(cpf) == None:
        print("O CPF não está cadastrado.")
        return False
    else:
        print("Usuário acessado.")
        return cpf

#CONTAS
def criar_conta(contas, usuario):

    indice = contas[usuario]

    if indice.get(1) == None:
        numero_da_conta = 1
    else:
        numero_da_conta = list(indice.keys())[-1] + 1

    contas[usuario][numero_da_conta] = dict()
    contas[usuario][numero_da_conta]['agencia'] = '0001'
    contas[usuario][numero_da_conta]['saldo'] = 0
    contas[usuario][numero_da_conta]['limite'] = 500
    contas[usuario][numero_da_conta]['extrato'] = ''
    contas[usuario][numero_da_conta]['numero_de_saques'] = 0
    contas[usuario][numero_da_conta]['LIMITE_SAQUES'] = 3

    return f"Conta número {numero_da_conta} criada"

def acessar_conta(contas, usuario):
    conta = int(input('Insira o número da conta =>'))

    indice = contas[usuario]

    if indice.get(conta) == None:
        print("Essa conta não existe.")
        return False
    else:
        print("Conta Acessada com sucesso.")
        return conta

#DEPOSITAR
def depositar(contas, usuario, conta):
    deposito = float(input('Digite o valor do deposito: '))

    if deposito > 0:
        contas[usuario][conta]['saldo'] += deposito
        contas[usuario][conta]['extrato'] += f"Depósito realizado no valor de: {deposito}\n"
        print(f"Seu saldo agora é {contas[usuario][conta]['saldo']:.2f}")
    else:
        print('Digite um valor maior que zero!')

#SACAR
def sacar(contas, usuario, numero_da_conta):
    limite = contas[usuario][numero_da_conta]['limite']
    numero_de_saques = contas[usuario][numero_da_conta]['numero_de_saques']
    LIMITE_SAQUES = contas[usuario][numero_da_conta]['LIMITE_SAQUES']
    saldo_atual = contas[usuario][numero_da_conta]['saldo']

    if numero_de_saques >= LIMITE_SAQUES:
        print(f'Você já alcançou o limite de saques diários')
        return False
    
    saque = float(input('Digite o valor do saque: '))
    
    if saque <= 0:
        print("O valor deve ser maior que zero!")
        return False

    elif (saldo_atual - saque) < 0:
        print(f'Você não pode sacar esse valor, não tem saldo suficiente!')

    elif saque > limite:
        print(f'O limite de saque é {limite}')

    elif saque <= saldo_atual and saque <= limite and numero_de_saques < 3 and (saldo_atual - saque >= 0):
        contas[usuario][numero_da_conta]['saldo'] -= saque
        contas[usuario][numero_da_conta]['numero_de_saques'] += 1
        contas[usuario][numero_da_conta]['extrato'] += f"Saque realizado no valor de: {saque}\n"
        print(f"Seu saldo agora é {contas[usuario][numero_da_conta]['saldo']:.2f}")

    else:
        print('Ocorreu um problema!')

#EXTRATO
def exibir_extrato(contas, usuario, conta):
    extrato = contas[usuario][conta]['extrato']
    saldo = contas[usuario][conta]['saldo']

    print(f'{extrato}') if extrato != '' else print('Não foram realizadas movimentações.')
    print(f'Saldo Atual: {saldo:.2f}')

#VARIÁVEIS
usuarios = dict()

contas = dict()

usuario = False

conta = False

#INTERFACE DO SISTEMA
while True:

    #USUÁRIOS
    if usuario == False:
        opcao_usuarios = input(menu_usuarios)

        ###CRIAR USUÁRIO
        if opcao_usuarios == '0':
            print(criar_usuario(usuarios, contas))

        ###ACESSAR USUÁRIO
        elif opcao_usuarios == '1':
            usuario = acessar_usuario(usuarios)

        ###SAINDO DO SISTEMA
        elif opcao_usuarios == '2':
            print("Saindo do sistema. Obrigado pela preferência!")
            break

        else:
            print("Comando inválido!")

    #CONTAS
    if conta == False and usuario != False:
        opcao_conta = input(menu_conta)

        ###CRIAR CONTA
        if opcao_conta == '0':
            print(criar_conta(contas, usuario))

        ###ACESSAR CONTA
        elif opcao_conta == '1':
            conta = acessar_conta(contas, usuario)

        #SAINDO DO USUÁRIO
        elif opcao_conta == '2':
            print("Saindo do usuário...")
            usuario = False
            continue

        else:
            print("Comando inválido!")
    
    #VERIFICAÇÃO DE LOGIN
    if conta == False or usuario == False:
        continue

    #ACTIONS
    opcao_actions = input(menu_actions)

    if opcao_actions == '0':
        depositar(contas, usuario, conta)

    elif opcao_actions == '1':
        sacar(contas, usuario, conta)

    elif opcao_actions == '2':
        exibir_extrato(contas, usuario, conta)

    elif opcao_actions == '3':
        print('Saindo da conta...')
        conta = False
        continue

    else:
        print('Opção inválida!')
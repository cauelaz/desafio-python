menu = """
    "[d]: deposito"
    "[s]: saque"
    "[e]: extrato"
    "[q]: sair"
=>"""
saques = 0
limite_saques = 3
extrato = ''
numero_saque = 0
saldo = 0

while True:
    opcao = input(menu)

    if opcao == "d":
        valor = float(input("Informe o valor de depósito:"))
        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"
        else:
            print("Operação falhou! Valor informado inválido")


    elif opcao == "s":
        valor_saque = float(input("Informe o valor de saque:"))
        excedeu_saldo = valor_saque > saldo
        excedeu_saques = numero_saque >= limite_saques
        
        if excedeu_saldo:
            print("Operação falhou! Você não tem saldo suficiente!")
        elif excedeu_saques:
            print("Operação falhou! Você atingiu o limite de saques!")
        elif valor_saque > 0:
            saldo -= valor_saque
            extrato += f"Saque: R$ {valor_saque:.2f}\n"
            numero_saque += 1
        else:
            print("Operação falhou! Valor informado inválido")

    elif opcao == "e":
        print("\n============EXTRATO=============")
        print("Não foram realizadas movimentações!") if not extrato else print(extrato)
        print(f"\n Saldo: R$ {saldo:.2f}")
        print("==================================")
    elif opcao == "q":
        break
    else:
        print("Opção Inválida! Tente novamente.")

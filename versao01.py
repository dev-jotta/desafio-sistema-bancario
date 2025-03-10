MENU = """

[D] Depositar
[S] Sacar
[E] Extrato
[Q] Sair

=> """

SALDO = 0
LIMITE = 500
EXTRATO = " "
NUMERO_SAQUES = 0
LIMITE_SAQUES = 3

while True:

    opcao = input(MENU)

    if opcao == "D":
        valor = float(input("Informe o valor do Depósito: "))

        if valor > 0:
            SALDO += valor
            EXTRATO += f"Depósito: R$ {valor:.2f}\n"

        else:
            print("A operação falhou, o valor informado é inválido!")

    elif opcao == "S":
        valor = float(input("Informe o valor do saque: "))

        excedeu_saldo = valor > SALDO
        excedeu_limite = valor > LIMITE
        EXCEDEU_SAQUE = NUMERO_SAQUES >= LIMITE_SAQUES

        if excedeu_saldo:
            print("A operação falhou, você não tem saldo suficiente!")

        elif excedeu_limite:
            print("A operação falhou, o valor do saque excedeu o limite!")

        elif EXCEDEU_SAQUE:
            print("A operação falhou, número máximo de saques excedido!")

        elif valor > 0:
            SALDO -= valor
            EXTRATO += f"Saque: R$ {valor:.2f}\n"
            NUMERO_SAQUES += 1

        else:
            print("A operação falhou, o valor informado é inválido!")

    elif opcao == "E":
        print("\n========== EXTRATO ==========")
        print("Não foram realizadas movimentações," if not EXTRATO
              else EXTRATO)
        print("\nSaldo: R$ {saldo:.2f}")
        print("===============================")

    elif opcao == "Q":
        break

    else:
        print("Operação inválida, por favor seleciona a opção desejada!")

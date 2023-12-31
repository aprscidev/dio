#Desafio: Criar um sistema bancário

menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = input(menu)

    if opcao == "d":
        valor = float(input("Informe o valor do depósito: "))

        if valor > 0:
            saldo = saldo + valor
            extrato += f"Depósito: R$ {valor:.2f}\n"

        else:
            print("O valor informado é inválido.")

    elif opcao == "s":
        valor = float(input("Informe o valor do saque: "))
        
        if valor > saldo:
            print("Saldo insuficiente.")
        
        elif valor > limite:
            print("Valor do saque ultrapassa o limite.")
        
        elif numero_saques >= LIMITE_SAQUES:
            print("Número de saques excedido.")

        elif valor > 0:
            saldo = saldo - valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saques = numero_saques + 1

        else:
            print("Valor informado inválido para concluir o saque.")

    elif opcao == "e":
        print("\n=============== EXTRATO ===============")
        print("Não foram realizadas transações bancárias." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("========================================")
    
    elif opcao == "q":
        break
    
    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")
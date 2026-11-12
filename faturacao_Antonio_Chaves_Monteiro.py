# António Chaves N. Monteiro

print("===== SISTEMA DE FATURAÇÃO =====\n")
qtde = int(input("Quantas compras deseja registar?: "))
for i in range(1, qtde + 1):
    print(f"\n----- Compra {i} de {qtde} -----")

    nome = input("Nome do cliente: ")
    genero = input("Género (M/F): ").upper()
    valor_compras = float(input("Valor total das compras: "))

    # Condições de prioridade
    gravida = input("É gestante? (S/N): ").upper()
    idoso = input("É pessoa idosa (65+ anos)? (S/N): ").upper()
    deficiencia = input("Tem deficiência? (S/N): ").upper()

    if valor_compras >= 100000:
        bonus = valor_compras * 0.10
    else:
        bonus = 0

    valor_final = valor_compras - bonus

    # Verificação de prioridade
    prioridade = (gravida == "S") or (idoso == "S") or (deficiencia == "S")

    # Apresentação da fatura
    print("\n========== FATURA ==========")
    print("Cliente:", nome)
    print("Género:", genero)
    print("Valor das Compras:", valor_compras, "Kz")
    print("Bónus (10%):", bonus, "Kz")
    print("Valor a Pagar:", valor_final, "Kz")
    print("=============================")

    if bonus > 0:
        print("O cliente tem direito a bónus de 10%.")
    else:
        print("O cliente não atingiu o valor mínimo para bónus.")

    if prioridade:
        print("Atendimento: PRIORITÁRIO.")
    else:
        print("Atendimento: ordem normal de chegada.")

print("\n===== FIM DO ATENDIMENTO. Total de clientes registados:", qtde, "=====")

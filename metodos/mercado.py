def interfaceEstoque(estoque):
    print(f"+----------------------------+")
    for i in range(len(estoque)):
        print(f"|{i+1}.{estoque[i][0].capitalize()} = R${estoque[i][1]} -- Quantidade: {estoque[i][2]}")
    print(f"+----------------------------+")

def calcular_carrinho(estoque, item, quantidade):
    carrinho = 0
    for items in estoque:
        if item in items:
            carrinho += items[1] * quantidade
    
    return carrinho

def setor_frutas():
    estoque = [["banana", 2, 15],["goiaba",3, 20],["pera", 7, 25]]
    interfaceEstoque(estoque)
    carrinho = 0
    while True:
        item = input("Escolha o item que deseja comprar: ").lower()
        quantidade = int(input("Digite a quantidade desse item: "))
        carrinho += calcular_carrinho(estoque, item, quantidade)
        sair = input("Deseja continuar nas compras s/n: ").lower()
        if sair == "s": 
            continue
        elif sair == "n":
            break
    print(f"O valor a se pagar e de R${carrinho}")
    return carrinho

def setor_limpeza():
    estoque = [["detergente", 5, 15],["bucha",0.5, 20],["desodorante", 1.5, 20],["desinfetante", 10, 5]]
    interfaceEstoque(estoque)
    carrinho = 0
    while True:
        item = input("Escolha o item que deseja comprar: ").lower()
        quantidade = int(input("Digite a quantidade desse item: "))
        carrinho += calcular_carrinho(estoque, item, quantidade)
        sair = input("Deseja continuar nas compras s/n: ").lower()
        if sair == "s": 
            continue
        elif sair == "n":
            break
    print(f"O valor a se pagar e de R${carrinho}")
    return carrinho

def setor_alimentos():
    estoque = [["macarrao", 2, 15],["biscoito",3, 20],["arroz", 7, 25],["feijao", 4, 10],["carne", 20, 10]]
    interfaceEstoque(estoque)
    carrinho = 0
    while True:
        item = input("Escolha o item que deseja comprar: ").lower()
        quantidade = int(input("Digite a quantidade desse item: "))
        carrinho += calcular_carrinho(estoque, item, quantidade)
        sair = input("Deseja continuar nas compras s/n: ").lower()
        if sair == "s": 
            continue
        elif sair == "n":
            break
    print(f"O valor a se pagar e de R${carrinho}")
    return carrinho

def loja():
    print("|=> Setor de Compras")
    print("|1.frutas\n|2.Alimentação\n|3.Limpeza\n|4.Voltar")

def finalizar_compra(carrinho):
        print("|=> Seu Carrinho:")
        print(f"O valor total do seu carrino foi de: R${carrinho}")
        valor = input("Deseja finalizar sua compra? s/n: ").lower()
        if valor == "s":
            print("Sua compra foi finalizada")
            print("Obrigado pela preferencia!!")
            exit()
        elif valor == "n":
            voltar = input("Ok! deseja continuar suas compras? s/n: ")
            if voltar == "s":
                print("Voltando!")
            elif voltar == "n":
                print("Ok entao seu carrinho sera excluido!!")
                carrinho = 0
            
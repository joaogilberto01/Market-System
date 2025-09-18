def cabecalho():
    print("=" * 50)
    print("🛒 BIG 3 SUPERMERCADO 🛒".center(50))
    print("=" * 50)
    
#função que registra o usuario com nome e senha em um arquivo .txt
def registros():
 cabecalho()
 while True:
    print("|Cadastramento => Registro")
    nome = input("Digite seu nome: ").strip()
    if verificarUsuariodisponivel(nome):
      #print("Registrando novo usúario...")
      cadastro = open("arquivos/usuarios.txt", "a")
      senha = input("Digite sua senha: ").strip()
      usuario = nome + "#" + senha
      cadastro.write(str(usuario) + "\n")
      cadastro.close()
      print("PERFIL CADASTRADO COM SUCESSO!")
      #print(f"Bem vindo {nome}")
      menu_principal()
      break
    else:
      print("Tente novamente")
      continue

# função que chama o aquivo usuario é le se ele existe!
def login():
    cabecalho()
    print("| Cadastramento => Login |")
    cadastro = open("arquivos/usuarios.txt", "r")
    nome = input("digite o nome: ").strip()
    senha = input("digite a senha: ").strip()
    for linha in cadastro:
        linha_lida = linha.strip().split("#")
        if linha_lida[0] == nome and linha_lida[1] == senha:
         cadastro.close()
         print(f"Login realizado com seucesso, Seja bem vindo(a) {linha_lida[0]}!")
         return True
    cadastro.close()
    print("Usuário ou senha incorretos!")
    return False

def menu_principal():
    while True:
        cabecalho()
        numero = int(input("1-Olhar produtos 🔎\n2-Finalizar Compra 🛒\n3-Voltar ⬅\n"))
        if numero == 1:
            mercado()
        elif numero == 2:
            print("Até a proxima")
            break
        else:
            break

def menu_cadastrar(): #menu inicial que da origem ao programa
    while True:
        cabecalho()
        print("| Cadastramento |")
        numero = int(input("1-Registrar\n2-Login\n3-Sair\n"))
        if numero == 1:
            registros()
        elif numero == 2:
            while True:
                loginstatus = login()
                if loginstatus == True:
                    menu_principal()
                    break  # Sai do while de login
                else:
                    print("Tente novamente!")
        elif numero == 3:
            print("Até a proxima")
            break # Sai do while principal
        else:
            print("Valor Invalido!")
            continue


def verificarUsuariodisponivel(nome):
    verificar = open("arquivos/usuarios.txt","r")
    for usuarios in verificar:
        nomeapenas = usuarios.strip().split("#")
        if nome == nomeapenas[0]:
            print(f"Infelizmente o nome de usuario: ({nome}) já está em uso 😭\nTente outro...")
            verificar.close()
            return False
    verificar.close()
    return True

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
    cabecalho()
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

def setor_alimentos():
    cabecalho()
    estoque = [["macarrao", 2, 15],["biscoito",3, 20],["arroz", 7, 25],["feijao", 4, 10]]
    interfaceEstoque(estoque)
    item = input("Escolha o item que deseja comprar: ").lower()
    quantidade = int(input("Digite a quantidade desse item: "))
    carrinho = calcular_carrinho(estoque, item, quantidade)
    print(f"O valor a se pagar e de R${carrinho}")
    return carrinho

def mercado():
    carrinho_final = 0
    while True:
        cabecalho()
        print("|Setor de Compras")
        print("|1.frutas\n|2.Alimentação\n|3.Limpeza|4.Voltar")
        entrada = int(input())
        if entrada == 1:
            carrinho1 = setor_frutas()
            carrinho_final += carrinho1
        elif entrada == 2:
            carrinho2 = setor_alimentos()
            carrinho_final += carrinho1
        elif entrada == 4:
            break
    return carrinho_final

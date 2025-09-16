def cabecalho():
    print("="*20,"| Mercado Big3 |","="*20)

#função que registra o usuario com nome e senha em um arquivo .txt
def registros():
 while True:
    cabecalho()
    print("|Cadastramento => Registro")
    nome = input("Digite seu nome: ").strip()
    if verificarUsuariodisponivel(nome):
      print("Registrando novo usúario...")
      cadastro = open("arquivos/usuarios.txt", "a")
      senha = input("Digite sua senha: ").strip()
      usuario = nome + "#" + senha
      cadastro.write(str(usuario) + "\n")
      cadastro.close()
      print("PERFIL CADASTRADO COM SUCESSO!")
      print(f"Bem vindo {nome}")
      menu_principal()
      break
    else:
      print("Tente novamente")
      continue

# função que chama o aquivo usuario é le se ele existe!
def login():
    print("="*20,"| Cadastramento => Login |","="*20)
    cadastro = open("arquivos/usuarios.txt", "r")
    nome = input("digite o nome: ").strip()
    senha = input("digite a senha: ").strip()
    for linha in cadastro:
        linha_lida = linha.strip().split("#")
        if linha_lida[0] == nome and linha_lida[1] == senha:
         cadastro.close()
         print("LOGIN REALIZADO COM SUCESSO!!!!!")
         print(f"SEJA BEM VINDO, {linha_lida[0]}!")
         return True
    
    cadastro.close()
    print("Usuário ou senha incorretos!")
    return False

def menu_principal():
    while True:
        cabecalho()
        numero = int(input("1-Comprar\n2-Historico\n3-Voltar\n"))
        if numero == 1:
            menu_compras2()
        elif numero == 3:
            print("Até a proxima")
            break
        else:
            break
#mudança de hugo
def menu_cadastrar():
    while True:
        print("="*20,"| Cadastramento |","="*20)
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


def verificarUsuariodisponivel(nome):
    verificar = open("arquivos/usuarios.txt","r")
    for usuarios in verificar:
        nomeapenas = usuarios.strip().split("#")
        if nome == nomeapenas[0]:
            print("O nome não está disponivel")
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
    estoque = [["banana", 2, 15],["goiaba",3, 20],["pera", 7, 25]]
    interfaceEstoque(estoque)
    item = input("Escolha o item que deseja comprar: ").lower()
    quantidade = int(input("Digite a quantidade desse item: "))
    carrinho = calcular_carrinho(estoque, item, quantidade)
    print(f"O valor a se pagar e de {carrinho}")


def mercado():
    cabecalho()
    print("|Setor de Compras")
    print("|1.frutas\n|2.comida\n|3.limpeza\n")
    entrada = int(input())


setor_frutas()

    
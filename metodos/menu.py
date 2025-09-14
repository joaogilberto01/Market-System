def cabecalho():
    print("="*20,"| Mercado Big3 |","="*20)

#função que registra o usuario com nome e senha em um arquivo .txt
def registros():
    cabecalho()
    print("|Cadastramento => Registro")
    cadastro = open("arquivos/usuarios.txt", "a")
    nome = input("Digite seu nome: ").strip()
    senha = input("Digite sua senha: ").strip()
    usuario = nome + "#" + senha
    cadastro.write(str(usuario) + "\n")
    cadastro.close()
    print("PERFIL CADASTRADO COM SUCESSO!")
    if login():
        menu_principal()

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
            menu_compras()
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

def menu_compras():
    ESTOQUE = {
    "Frutas":["pera","morango","banana","goiaba"],
    "Limpeza":["detergente","sabão","desinfetante"],
}
    
    cabecalho()
    carrinho = []

    for key in ESTOQUE.keys():
        print(f"|{key} >> :{ESTOQUE[key]}")

    while True:
        valor = input("Qual produto você deseja comprar: ")
        quant = int(input(f"Digite a quantidade do(a) {valor}!\n"))
        for i in ESTOQUE.keys():
            if valor in ESTOQUE[i]:
                for i in range(quant):
                    carrinho.append(valor)
        
        print("Seu carrinho com seus itens:", carrinho)
        sair = input("Deseja continuar? s/n\n").lower()
        if sair == "n":
            break
        elif sair == "s":
            continue
        else:
            print("Valor indefinido!")
            break

def menu_compras2():
    ESTOQUE2 = {"banana":2,"goiaba":3,"chiclete":0.5
    }
    conta = 0

    for key, value in ESTOQUE2.items():
        print(f"{key} - R${value}")

    while True:
        valor = input("Digite o que deseja comprar: ")
        quant = int(input(f"Digite a quantidade do(a) {valor}: "))
        
        for key, value in ESTOQUE2.items():
            if valor in ESTOQUE2:
                conta = value*quant
        print(f"o valor total a se pagar agora é de: R${conta}")
        sair = input("Deseja continuar a fazer compras? s/n\n").lower()
        if sair == "n":
            continue
        elif sair == "s":
            break
        else:
            print("valor indefinido!")
            break



menu_compras2()
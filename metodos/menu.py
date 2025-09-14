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
    print("Perfil cadastrado")

# função que chama o aquivo usuario é le se ele existe!
def login():
    cabecalho()
    print("| Cadastramento => Login")
    cadastro = open("arquivos/usuarios.txt", "r")
    nome = input("digite o nome: ").strip()
    senha = input("digite a senha: ").strip()
    for linha in cadastro:
        linha_lida = linha.strip().split("#")
        if linha_lida[0] == nome and linha_lida[1] == senha:
            cadastro.close()
            print(f"Seja Bem Vindo {linha_lida[0].capitalize()} !")
            return True

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

def menu_cadastrar():
    while True:
        cabecalho()
        print("| Cadastramento")
        numero = int(input("1-Registrar\n2-Login\n3-Anônimo\n4-Sair\n"))
        if numero == 1:
            registros()
            continue
        if numero == 2:
            if login():
                menu_principal()
        if numero == 3:
                menu_principal()
        if numero == 4:
            print("Até a proxima")
            break

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
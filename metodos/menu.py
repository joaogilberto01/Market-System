def cabecalho():
    print("="*20,"| Mercado Big3 |","="*20)
    
#função que registra o usuario com nome e senha em um arquivo .txt
def registros():
    cabecalho()
    print("|Cadastramento => Registro")
    cadastro = open("Arquivos/Usuarios.txt", "a")
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
    cadastro = open("Arquivos/Usuarios.txt", "r")
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
        numero = int(input("1-Compra\n2-Historico\n3-Sair\n"))
        if numero > 0:
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
        if numero == 4:
            print("Até a proxima")
            break
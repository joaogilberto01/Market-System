#função que registra o usuario com nome e senha em um arquivo .txt
def registros():
    print("="*20,"| Cadastramento => Registro |","="*20)
    cadastro = open("Arquivos/Usuarios.txt", "a")
    nome = input("Digite seu nome: ").strip()
    senha = input("Digite sua senha: ").strip()
    usuario = nome + "#" + senha
    cadastro.write(str(usuario) + "\n")
    cadastro.close()
    print("Perfil cadastrado")

# função que chama o aquivo usuario é le se ele existe!
def login():
    print("="*20,"| Cadastramento => Login |","="*20)
    cadastro = open("Arquivos/Usuarios.txt", "r")
    nome = input("digite o nome: ").strip()
    senha = input("digite a senha: ").strip()
    for linha in cadastro:
        linha_lida = linha.strip().split("#")
        if linha_lida[0] == nome and linha_lida[1] == senha:
            cadastro.close()
            print(f"Seja Bem Vindo {linha_lida[0]}")
            return True

def menu_principal():
    while True:
        print("="*20,"| Bem Vindo ao Mercado Big3 |","="*20)
        numero = int(input("1-Compra\n2-Historico\n3-Sair\n "))
        if numero > 0:
            break

def menu_cadastrar():
    while True:
        print("="*20,"| Cadastramento |","="*20)
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
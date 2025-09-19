import hashlib

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

def login():
    print("| Cadastramento => Login |")
    cadastro = open("arquivos/usuarios.txt", "r")
    nome = input("digite o nome: ").strip()
    senha = input("digite a senha: ").strip()
    hashSenha = hashlib.sha256(senha.encode("utf-8")).hexdigest()
    for linha in cadastro:
        linha_lida = linha.strip().split("#")
        if linha_lida[0] == nome and linha_lida[1] == hashSenha:
         cadastro.close()
         print(f"Login realizado com seucesso, Seja bem vindo(a) {linha_lida[0]}!")
         return True
    cadastro.close()
    print("============================")
    print("Usuário ou senha incorretos!")
    print("============================")
    return False

def registros():
    print("|Cadastramento => Registro")
    nome = input("Digite seu nome: ").strip()
    if verificarUsuariodisponivel(nome):
      cadastro = open("arquivos/usuarios.txt", "a")
      senha = input("Digite sua senha: ").strip()
      usuario = nome + "#" + senha
      hashSenha = hashlib.sha256(senha.encode("utf-8")).hexdigest()
      usuario = nome + "#" + hashSenha
      cadastro.write(str(usuario) + "\n")
      cadastro.close()
      print("PERFIL CADASTRADO COM SUCESSO!")

def exclusaodeconta():
   print("Excluindo conta...")
   exclusao = open("arquivos/usuarios.txt","r")
   nome = input("Digite seu nome de usuario novamente: ")
   lista_usuarios = []
   for usuarios in exclusao:
      nomedousuario = usuarios.strip().split("#")
      if nome != nomedousuario[0]:
         lista_usuarios.append(usuarios)
   exclusao.close()
   inclusao = open("arquivos/usuarios.txt" , "w")
   for usuariosreescritos in lista_usuarios:
      inclusao.write(usuariosreescritos)
   print(f"O Usuario {nome} foi excluido com sucesso!")
   inclusao.close()
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
       tentarnovamente = input("Você deseja tentar se registrar novamente? S/N?").capitalize()
       if tentarnovamente == "N":
          print("Poxa, que pena!")
          print("voltando ao menu principal...")
          break
       else:
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
        numero = int(input("1-Comprar\n2-Historico\n3-Sair da conta\n4-Excluir conta\n"))
        if numero == 1:
            menu_compras()
        elif numero == 3:
            print(f"Até a proxima")
            break
        elif numero == 4:
            while True:
             exclusao = input("Você tem certeza que quer excluir a conta? S/N?").capitalize()
             if exclusao == "N":
                break
             elif exclusao == "S":
                exclusão2 = input("Você tem certeza MESMO? S/N?").capitalize()
                if exclusão2 == "N":
                   print("Obrigado por repensar na sua escolha!")
                   break
                elif exclusão2 == "S":
                   exclusaodeconta()
                   return True
                   
        else:
            break
#mudança de hugo
def menu_cadastrar():
    while True:
        print("="*20,"| Cadastramento |","="*20)
        numero = int(input("1-Registrar\n2-Login\n3-Encerrar o programa\n"))
        if numero == 1:
            registros()
        elif numero == 2:
            while True:
                loginstatus = login()
                if (loginstatus == True):
                    resultadodaexclusao = menu_principal()
                    if (resultadodaexclusao == True):
                       return
                    break  # Sai do while de login
                else:
                    print("Usuario ou senha errados!")
                    pergunta = input("Você deseja tentar novamente fazer o login? S/N").capitalize()
                    if (pergunta != "S"):
                        break

                    
        elif numero == 3:
            print("Muito obrigado por utilizar o Mercado Big3! Até a próxima!")
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

def exclusaodeconta():
   print("Excluindo conta...")
   exclusao = open("arquivos/usuarios.txt","r")
   nome = input("Digite seu nome de usuario novamente")
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
   menu_cadastrar()
      

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

      


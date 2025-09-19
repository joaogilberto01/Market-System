import metodos.menu as menu
import metodos.mercado as mercado
import metodos.registro as rg

while True:
    menu.cabecalho()
    menu.menu_inicial()
    valor = int(input())

    if valor == 1:
        menu.cabecalho()
        rg.registros()

    elif valor == 2:
        menu.cabecalho()
        if rg.login():
            carrinho_final = 0
            while True:
                menu.cabecalho()
                menu.menu_principal()
                entrar = int(input(""))
                if entrar == 1:
                    menu.cabecalho()
                    mercado.loja()

                    entrada = int(input())
                    if entrada == 1:
                        menu.cabecalho()
                        carrinho1 = mercado.setor_frutas()
                        carrinho_final += carrinho1

                    elif entrada == 2:
                        menu.cabecalho()
                        carrinho2 = mercado.setor_alimentos()
                        carrinho_final += carrinho2

                    elif entrada == 3:
                        menu.cabecalho()
                        carrinho3 = mercado.setor_limpeza()
                        carrinho_final += carrinho3

                    elif entrada == 4:
                        break
                        
                elif entrar == 2:
                    menu.cabecalho()
                    mercado.finalizar_compra(carrinho_final)

                elif entrar == 3:
                    break

                elif entrar == 4:
                    rg.exclusaodeconta()

    elif valor == 3:
        print("Até logo!!")
        break
import hashlib

#cabelho do mercado
def cabecalho():
    print("=" * 50)
    print("🛒 BIG 3 SUPERMERCADO 🛒".center(50))
    print("=" * 50)

def menu_inicial():
    print("| Cadastramento |")
    print("|1-Registrar\n|2-Login\n|3-Sair")

def menu_principal():
    print("1-Olhar produtos 🔎\n2-Finalizar Compra 🛒\n3-Voltar ⬅\n4-Excluir Conta ❌")
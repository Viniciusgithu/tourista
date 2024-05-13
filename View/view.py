# view.py: Este é o arquivo onde você define suas funções de visualização.

# Responsável por apresentar os dados ao usuário;
# Coletar entrada do usuário;
# Lida com a interface do usuário;
# Apresenta os dados de uma maneira que seja compreensível e interativa.


def exibir_menu():
    print("MENU COM AS PRINCIPAIS OPÇÕES VISÍVEIS PARA O TURISTA")

def solicitar_login():
    nome = input("Digite seu nome de usuário: ")
    senha = input("Digite sua senha: ")
    return nome, senha

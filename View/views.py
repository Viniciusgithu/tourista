# view.py: Este é o arquivo onde você define suas funções de visualização.

# Responsável por apresentar os dados ao usuário;
# Coletar entrada do usuário;
# Lida com a interface do usuário;
# Apresenta os dados de uma maneira que seja compreensível e interativa.


class MenuView:
    @staticmethod
    def mostrar_menuBusca():
        print("=" * 40)
        print("Escolha uma opção:")
        print("1. Ver informações sobre um ponto turístico")
        print("2. Adicionar um novo ponto turístico")
        print("3. Editar ponto turístico")
        print("4. Excluir ponto turístico")
        print("5. Sair")
        print("=" * 40)
    
    @staticmethod
    def menu_principal():      
        print("Bem-vindo(a) ao Tourista!")
        print("1. Recife Antigo")
        print("2. Alto da Sé")
        print("3. Cristo Redentor")
        print("4. Torre Eiffel")
        print("5. Coliseu")
        print("6. Palacio de Buckingham")
        print("7. Buscar outro ponto turístico, adicionar, editar ou excluir um ponto turistico.")

    @staticmethod
    def obter_opcao():
        return input("Escolha uma opção: ")
class MenuView:
        
    @staticmethod
    def mostrar_menuBusca():
        print("")
        print("Opções disponíveis:")
        print("")
        print("  1. Ver informações sobre um ponto turístico e avaliar")
        print("  2. Adicionar um novo ponto turístico")
        print("  3. Editar ponto turístico")
        print("  4. Excluir ponto turístico")        
        print("  0. Voltar")
        print("")

    @staticmethod
    def menu_principal():
        print("")
        print("Bem-vindo(a) ao Tourista!")
        print("")
        print("Opções disponíveis:")
        print("")
        print("  1. Recife Antigo")
        print("  2. Alto da Sé")
        print("  3. Cristo Redentor")
        print("  4. Torre Eiffel")
        print("  5. Coliseu")
        print("  6. Palacio de Buckingham")
        print("  7. Buscar outro ponto turístico, avaliar, adicionar, editar ou excluir um ponto turistico")
        print("  0. Finalizar o programa")
        print("")      

    @staticmethod
    def mostrar_menuAvaliacao(cidade):
        print("")
        print("Opções disponíveis:")
        print("")        
        print("  1. Adicionar avaliação")
        print("  2. Atualizar avaliação")
        print("  3. Deletar avaliação")
        print("  0. Voltar")        
        print("")

    @staticmethod
    def obter_opcao():
        return input("Escolha uma opção: ")


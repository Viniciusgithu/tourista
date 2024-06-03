class MenuView:
        
    @staticmethod
    def mostrar_menuBusca():
        print("")
        print("O que você procura no Tourista?")
        print("")
        print("  1. Ver informações sobre um ponto turístico e avaliar 🔍")
        print("  2. Adicionar um novo ponto turístico ✅")
        print("  3. Editar ponto turístico ✏️")
        print("  4. Excluir ponto turístico 🗑️")        
        print("  0. Voltar para o menu principal ❌")
        print("")

    @staticmethod
    def menu_principal():
        print("")
        print("Bem-vindo(a) ao Tourista!")
        print("")
        print("O Tourista indica os pontos turísticos mais visitados, que tal escolher um deles? 🤔")
        print("")
        print("  1. Recife Antigo 🥇")
        print("  2. Alto da Sé 🥈")
        print("  3. Cristo Redentor 🥉")
        print("  4. Torre Eiffel 🏅")
        print("  5. Coliseu 🏅")
        print("  6. Cataratas do Iguaçu 🏅")
        print("  7. Que tal você buscar um ponto turístico? 🔍")
        print("  0. Sair do Tourista ❌")
        print("")

    @staticmethod
    def mostrar_menuAvaliacao(cidade):
        print("")
        print("Deseja avaliar este ponto turístico? ")
        print("")        
        print("  1. Adicionar avaliação ✅")
        print("  2. Atualizar avaliação ⏳")
        print("  3. Deletar avaliação 🗑️")
        print("  0. Não desejo avaliar ❌")        
        print("")

    @staticmethod
    def obter_opcao():
        return input("Escolha uma opção: ")


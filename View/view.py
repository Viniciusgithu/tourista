# view.py: Este é o arquivo onde você define suas funções de visualização.

# Responsável por apresentar os dados ao usuário;
# Coletar entrada do usuário;
# Lida com a interface do usuário;
# Apresenta os dados de uma maneira que seja compreensível e interativa.

class AvaliacoesUsuarioView:
    @staticmethod
    def show_reviews(reviews):
        if reviews:
            for review in reviews:
                print(review)
        else:
            print('Nenhuma avaliação encontrada para a cidade.')

    @staticmethod
    def show_success(message):
        print(message)

    @staticmethod
    def show_error(message):
        print(message)

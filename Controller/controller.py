# controller.py: Este é o arquivo onde você define a lógica do seu aplicativo.

# O Controller é responsável por: 
# Receber as credenciais do usuário da View; 
# Interagir com o Modelo para verificar essas credenciais; 
# Notificar a View sobre o resultado do login.

class AvaliacoesUsuarioController:
    def __init__(self, model, view):
        self.model = model
        self.view = view

    def add_review(self, nome_usuario, cidade, avaliacao, comentario):
        review_id = self.model.add_review(nome_usuario, cidade, avaliacao, comentario)
        self.view.show_success('Avaliação adicionada com sucesso. ID: {}'.format(review_id))

    def read_reviews(self, cidade):
        reviews = self.model.read_reviews(cidade)
        self.view.show_reviews(reviews)

    def update_review(self, review_id, avaliacao, comentario):
        if self.model.update_review(review_id, avaliacao, comentario):
            self.view.show_success('Avaliação atualizada com sucesso.')
        else:
            self.view.show_error('Avaliação não encontrada.')

    def delete_review(self, review_id):
        if self.model.delete_review(review_id):
            self.view.show_success('Avaliação deletada com sucesso.')
        else:
            self.view.show_error('Avaliação não encontrada.')

    def run_menu(self):
        while True:
            print("\nEscolha uma operação:")
            print("1. Adicionar avaliação de uma cidade")
            print("2. Ler avaliações da cidade escolhida")
            print("3. Atualizar avaliação")
            print("4. Deletar avaliação")
            print("5. Sair")
            
            choice = input("Opção: ")
            
            if choice == '1':
                nome_usuario = input("Nome do usuário: ")
                cidade = input("Cidade: ")
                avaliacao = int(input("Nota (0-5): "))
                comentario = input("Comentário: ")
                self.add_review(nome_usuario, cidade, avaliacao, comentario)
            elif choice == '2':
                cidade = input("Cidade: ")
                self.read_reviews(cidade)

            elif choice == '3':
                review_id = int(input("ID da avaliação: "))
                avaliacao = int(input("Nova nota (0-5): "))
                comentario = input("Novo comentário: ")
                self.update_review(review_id, avaliacao, comentario)
            elif choice == '4':
                review_id = int(input("ID da avaliação: "))
                self.delete_review(review_id)
            elif choice == '5':
                break
            else:
                print("Opção inválida. Tente novamente.")


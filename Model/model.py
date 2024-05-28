# model.py: Este é o arquivo onde você define suas classes de dados e funções relacionadas.

# Representa os dados e a lógica de negócios da aplicação; 
# Ele gerencia os dados;
import json
import os

class AvaliacoesUsuarioModel:
    def __init__(self, file_path):
        self.file_path = file_path

    def load_json(self):
        if os.path.exists(self.file_path):
            with open(self.file_path, 'r') as file:
                return json.load(file)
        return []

    def save_json(self, data):
        with open(self.file_path, 'w') as file:
            json.dump(data, file, indent=4)

    def add_review(self, nome_usuario, cidade, avaliacao, comentario):
        reviews = self.load_json()
        review_id = len(reviews) + 1
        reviews.append({'id': review_id, 'nome_usuario': nome_usuario, 'cidade': cidade, 'avaliacao': avaliacao, 'comentario': comentario})
        self.save_json(reviews)
        return review_id

    def read_reviews(self, cidade):
        reviews = self.load_json()
        return [review for review in reviews if review['cidade'] == cidade]

    def update_review(self, review_id, avaliacao, comentario):
        reviews = self.load_json()
        for review in reviews:
            if review['id'] == review_id:
                review['avaliacao'] = avaliacao
                review['comentario'] = comentario
                self.save_json(reviews)
                return True
        return False

    def delete_review(self, review_id):
        reviews = self.load_json()
        updated_reviews = [review for review in reviews if review['id'] != review_id]
        if len(reviews) == len(updated_reviews):
            return False
        else:
            self.save_json(updated_reviews)
            return True

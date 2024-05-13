# model.py: Este é o arquivo onde você define suas classes de dados e funções relacionadas.

# Representa os dados e a lógica de negócios da aplicação; 
# Ele gerencia os dados;
# Implementa a lógica de negócios; 
# Interage com o banco de dados;
# Representa o estado atual da aplicação.

class Usuario:
    def __init__(self, nome, senha):
        self.nome = nome
        self.senha = senha

    def verificar_senha(self, senha):
        return self.senha == senha

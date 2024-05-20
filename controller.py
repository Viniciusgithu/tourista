# controller.py: Este é o arquivo onde você define a lógica do seu aplicativo.

# O Controller é responsável por: 
# Receber as credenciais do usuário da View; 
# Interagir com o Modelo para verificar essas credenciais; 
# Notificar a View sobre o resultado do login.


from Model import Usuario
from View import exibir_menu, solicitar_login

class Controller:
    def __init__(self):
        self.usuarios = [Usuario('admin', 'admin')]  # Exemplo de usuário

    def executar(self):
        nome, senha = solicitar_login()
        for usuario in self.usuarios:
            if usuario.nome == nome and usuario.verificar_senha(senha):
                exibir_menu()
                return
        print("Falha no login")
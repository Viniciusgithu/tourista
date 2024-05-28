import json

class UsuariosModel:
    def __init__(self):
        self.credenciais = self.carregar_usuarios()
    
    def carregar_usuarios(self):
        with open('usuarios.json', 'r') as arquivo:
            return json.load(arquivo)
    
    def salvar_usuarios(self):
        with open('usuarios.json', 'w') as arquivo:
            json.dump(self.credenciais, arquivo, indent = 3)
    
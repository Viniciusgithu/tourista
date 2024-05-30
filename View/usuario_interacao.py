class UsuarioInterface:
    def entrada(self, mensagem):
        return input(mensagem)
    
    def obter_mensagem(self, mensagem):
        print(mensagem)
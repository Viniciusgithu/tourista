import sys
from Controller.controllerUsuario import GerenciadorArquivosController

sys.path.append('controller')
sys.path.append('view')
sys.path.append('model')

def main():
    gerenciador = GerenciadorArquivosController()
    gerenciador.menu()

if __name__ == "__main__":
    main()
    
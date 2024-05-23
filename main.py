
import sys
sys.path.append('controller')
sys.path.append('view')
sys.path.append('model')

from Controller import GerenciadorArquivosController

if __name__ == "__main__":
    gerenciador = GerenciadorArquivosController()
    gerenciador.menu()
    



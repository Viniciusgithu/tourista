
import sys
sys.path.append('models')
sys.path.append('views')    
sys.path.append('controllers')
from Model.models import PontoTuristicoDAO
from Controller.controllers import TouristaController

def executa():
    ponto_turistico_dao = PontoTuristicoDAO('pontos_turisticos.json')
    tourista_controller = TouristaController(ponto_turistico_dao)
    tourista_controller.main()


if __name__ == '__main__':
    executa()
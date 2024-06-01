
import sys

sys.path.append('models')
sys.path.append('views')    
sys.path.append('controllers')

from Model.models import PontoTuristicoDAO, AvaliacoesDAO
from Controller.controllers import TouristaController, AvaliacoesController

def executa(usrLogado):
    ponto_turistico_dao = PontoTuristicoDAO('pontos_turisticos.json')
    tourista_controller = TouristaController(ponto_turistico_dao)
    
    tourista_controller.main(usrLogado)

if __name__ == '__main__':
    executa()
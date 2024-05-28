from Controller.controller import AvaliacoesUsuarioController
from Model.model import AvaliacoesUsuarioModel
from View.view import AvaliacoesUsuarioView

if __name__ == "__main__":
    REVIEWS_FILE = 'reviews.json'
    model = AvaliacoesUsuarioModel(REVIEWS_FILE)
    view = AvaliacoesUsuarioView()
    controller = AvaliacoesUsuarioController(model, view)
    controller.run_menu()


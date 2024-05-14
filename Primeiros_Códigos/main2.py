class PontoTuristico:
    def __init__(self, nome, local, descricao, horario_funcionamento, custo_entrada):
        self.nome = nome
        self.local = local
        self.descricao = descricao
        self.horario_funcionamento = horario_funcionamento
        self.custo_entrada = custo_entrada

class Menu:
    def mostrar_menu(self):
        print("Bem-vindo(a) ao Tourista!")
        print("Escolha uma opção:")
        print("1. Ver informações sobre um ponto turístico")
        print("2. Sair")

    def obter_opcao(self):
        return input("Escolha uma opção: ")

class Tourista:
    def __init__(self, pontos_turisticos):
        self.pontos_turisticos = pontos_turisticos

    def mostrar_informacoes(self, ponto):
        if ponto in self.pontos_turisticos:
            ponto_turistico = self.pontos_turisticos[ponto]
            print(f"Nome: {ponto_turistico.nome}")
            print(f"Local: {ponto_turistico.local}")
            print(f"Descrição: {ponto_turistico.descricao}")
            print(f"Horário de Funcionamento: {ponto_turistico.horario_funcionamento}")
            print(f"Custo de Entrada: {ponto_turistico.custo_entrada}")
            print()
        else:
            print("Ponto turístico não encontrado.")

    def main(self):
        menu = Menu()
        while True:
            menu.mostrar_menu()
            opcao = menu.obter_opcao()
            
            if opcao == "1":
                ponto = input("Digite o nome do ponto turístico: ")
                self.mostrar_informacoes(ponto)
            elif opcao == "2":
                print("Obrigado por usar o Tourista! Volte sempre!")
                break
            else:
                print("Opção inválida. Por favor, escolha uma opção válida.")

if __name__ == "__main__":
    pontos_turisticos = {
        "Recife Antigo": PontoTuristico("Recife Antigo", "Pernambuco - Brasil", "Centro histórico com muitos bares e restaurantes.", "24 horas", "Gratuito"), 
        "Parque das Ruínas": PontoTuristico("Parque das Ruínas","Pernambuco - Brasil","Parque com áreas verdes e ruínas históricas.","9:00 - 17:00","Gratuito"),
        "Parque da Jaqueira": PontoTuristico("Parque da Jaqueira","Pernambuco - Brasil","Parque arborizado com áreas para lazer e prática de esportes.","5:00 - 22:00","Gratuito"),
        "Museu Cais do Sertao": PontoTuristico("Museu Cais do Sertao","Pernambuco - Brasil","Museu dedicado à cultura nordestina, com exposições interativas.","9:00 - 17:00","R$ 10,00"),
        "Museu Ricardo Brennand": PontoTuristico("Pernambuco - Brasil","Museu de arte com coleções de armas, armaduras e obras de arte.","13:00 - 17:00 (fechado às segundas-feiras)","R$ 20,00"),
        "Alto da Sé": PontoTuristico("","","","",""),
    }
    tourista = Tourista(pontos_turisticos)
    tourista.main()

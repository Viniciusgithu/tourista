from Model.models import PontoTuristico, AvaliacoesUsuario, AvaliacoesDAO
from View.views import MenuView

class TouristaController:
    def __init__(self, ponto_turistico_dao):
        self.ponto_turistico_dao = ponto_turistico_dao

    def mostrar_informacoes(self, ponto):
        pontos_turisticos = self.ponto_turistico_dao.carregar_pontos_turisticos()
        for ponto_turistico in pontos_turisticos:
            if ponto_turistico.nome.lower() == ponto.lower():                
                print("=" * 100)
                print("")
                print(f"Informações do ponto turistico: {ponto.lower()}")
                print("")
                print("Nome: {}".format(ponto_turistico.nome.upper()))
                print("")
                print(f"  Local: {ponto_turistico.local}")
                print("")
                print(f"  Descrição: {ponto_turistico.descricao}")
                print("")
                print(f"  Horário de Funcionamento: {ponto_turistico.horario_funcionamento}")
                print("")
                print(f"  Custo de Entrada: {ponto_turistico.custo_entrada}")
                oAvaliacoesDAO = AvaliacoesDAO('reviews.json')
                print("")
                print(oAvaliacoesDAO.exibir_avaliacao(ponto_turistico.nome))                               
                print("")
                print("=" * 100)
                
                return ponto_turistico.nome             
        
        print("=" * 100)
        print("*****  Ponto turístico não encontrado.  *****")
        print("=" * 100)

        return ""

    def adicionar_ponto_turistico(self, nome, local, descricao, horario_funcionamento, custo_entrada):
        novo_ponto = PontoTuristico(nome, local, descricao, horario_funcionamento, custo_entrada)
        self.ponto_turistico_dao.adicionar_ponto_turistico(novo_ponto)

    def editar_ponto_turistico(self, nome, local, descricao, horario_funcionamento, custo_entrada):
        ponto_atualizado = PontoTuristico(nome, local, descricao, horario_funcionamento, custo_entrada)
        self.ponto_turistico_dao.editar_ponto_turistico(ponto_atualizado)

    def excluir_ponto_turistico(self, nome):
        self.ponto_turistico_dao.excluir_ponto_turistico(nome)

    def main(self, usrLogado):
        while True:
            MenuView.menu_principal()
            opcao = MenuView.obter_opcao()
            print("=" * 100)
            if opcao == "1":
                ponto = 'Recife Antigo'
                cidade = self.mostrar_informacoes(ponto)
                if cidade != "":
                    avaliacoes_dao = AvaliacoesDAO('reviews.json')    
                    avaliacoes_controller = AvaliacoesController(avaliacoes_dao)
                    avaliacoes_controller.run_menu(cidade, usrLogado) 
                    continue                 
            elif opcao == "2":
                ponto = 'Alto da Sé'
                cidade = self.mostrar_informacoes(ponto)
                if cidade != "":
                    avaliacoes_dao = AvaliacoesDAO('reviews.json')    
                    avaliacoes_controller = AvaliacoesController(avaliacoes_dao)
                    avaliacoes_controller.run_menu(cidade, usrLogado) 
                    continue   
            elif opcao == '3':
                ponto = 'Cristo Redentor'
                cidade = self.mostrar_informacoes(ponto)
                if cidade != "":
                    avaliacoes_dao = AvaliacoesDAO('reviews.json')    
                    avaliacoes_controller = AvaliacoesController(avaliacoes_dao)
                    avaliacoes_controller.run_menu(cidade, usrLogado) 
                    continue   
            elif opcao == '4':
                ponto = 'Torre Eiffel'
                cidade = self.mostrar_informacoes(ponto)
                if cidade != "":
                    avaliacoes_dao = AvaliacoesDAO('reviews.json')    
                    avaliacoes_controller = AvaliacoesController(avaliacoes_dao)
                    avaliacoes_controller.run_menu(cidade, usrLogado) 
                    continue   
            elif opcao == '5':
                ponto = 'Coliseu'
                cidade = self.mostrar_informacoes(ponto)
                if cidade != "":
                    avaliacoes_dao = AvaliacoesDAO('reviews.json')    
                    avaliacoes_controller = AvaliacoesController(avaliacoes_dao)
                    avaliacoes_controller.run_menu(cidade, usrLogado) 
                    continue   
            elif opcao == '6':
                ponto = 'Palacio de Buckingham'
                cidade = self.mostrar_informacoes(ponto)
                if cidade != "":
                    avaliacoes_dao = AvaliacoesDAO('reviews.json')    
                    avaliacoes_controller = AvaliacoesController(avaliacoes_dao)
                    avaliacoes_controller.run_menu(cidade, usrLogado) 
                    continue   
            elif opcao == '7':
                while True:
                    MenuView.mostrar_menuBusca()
                    sub_opcao = MenuView.obter_opcao()
                    print("=" * 100)
                    if sub_opcao == "1":
                        ponto = input("Digite o nome do ponto turístico: ").lower()
                        cidade = self.mostrar_informacoes(ponto)
                        if cidade != "":
                            avaliacoes_dao = AvaliacoesDAO('reviews.json')    
                            avaliacoes_controller = AvaliacoesController(avaliacoes_dao)
                            avaliacoes_controller.run_menu(cidade, usrLogado) 
                            break 

                    elif sub_opcao == "2":
                        nome = input("Digite o nome do novo ponto turístico: ")
                        local = input("Digite o local: ")
                        descricao = input("Digite a descrição: ")
                        horario_funcionamento = input("Digite o horário de funcionamento: ")
                        custo_entrada = input("Digite o custo de entrada: ")
                        self.adicionar_ponto_turistico(nome, local, descricao, horario_funcionamento, custo_entrada)

                    elif sub_opcao == "3":
                        nome = input("Digite o nome do ponto turístico a ser editado: ").lower()
                        local = input("Digite o novo local: ")
                        descricao = input("Digite a nova descrição: ")
                        horario_funcionamento = input("Digite o novo horário de funcionamento: ")
                        custo_entrada = input("Digite o novo custo de entrada: ")
                        self.editar_ponto_turistico(nome, local, descricao, horario_funcionamento, custo_entrada)

                    elif sub_opcao == "4":
                        nome = input("Digite o nome do ponto turístico a ser excluído: ").lower()
                        self.excluir_ponto_turistico(nome)
                        print("")
                        print(f"Ponto turístico: {nome}, foi excluído com sucesso! ")
                        print("====================================================================================================")

                    elif sub_opcao == "0":
                        break
                    else:
                        print("Opção inválida. Por favor, escolha uma opção válida.")
                        
            elif opcao == '0':
                print("Programa finalizado.")
                exit()
            else:
                print("Opção inválida. Por favor, escolha uma opção válida.")
                continue

class AvaliacoesController:
    def __init__(self, avaliacoes_dao):
        self.avaliacoes_dao = avaliacoes_dao

    def adicionar_avaliacao(self, nome_usuario, cidade, avaliacao):
        nova_avaliacao = AvaliacoesUsuario(nome_usuario, cidade, avaliacao)
        oAvaliacoesDAO = AvaliacoesDAO('reviews.json') 
        oAvaliacoesDAO.adicionar_avaliacoes(nova_avaliacao)

    def editar_avaliacao(self, nome_usuario, cidade, avaliacao):
        avaliacao = AvaliacoesUsuario(nome_usuario, cidade, avaliacao)
        oAvaliacoesDAO = AvaliacoesDAO('reviews.json') 
        oAvaliacoesDAO.editar_avaliacoes(avaliacao)
    
    def excluir_avaliacao(self, nome_usuario, cidade):
        avaliacao = AvaliacoesUsuario(nome_usuario, cidade, 0)
        oAvaliacoesDAO = AvaliacoesDAO('reviews.json') 
        oAvaliacoesDAO.excluir_avaliacoes(avaliacao)

    def existe_avaliacao(self, cidade, usrLogado):
        avaliacoes_dao = AvaliacoesDAO('reviews.json')    
        reviews = avaliacoes_dao.load_json()
        for review in reviews:
            if review['usuario'] == usrLogado.lower() and review['cidade'] == cidade.lower():
                return True
        return False 
        
    def run_menu(self, cidade, usrlogado):
        while True:
            MenuView.mostrar_menuAvaliacao(cidade)
            opcMenuAvalia = MenuView.obter_opcao()
            print("=" * 100) 
            if opcMenuAvalia == '1':
                if self.existe_avaliacao(cidade, usrlogado):
                    print("Voçê já avaliou esse ponto turistico!")
                    continue       
                         
                while True:
                    avaliacao = float( input("Nota (0-5): ") )
                    if avaliacao < 0 or avaliacao > 5:
                        print("Informa um valor entre (0-5)")
                        continue
                    else:
                        break
                self.adicionar_avaliacao(usrlogado, cidade, avaliacao)
                break

            elif opcMenuAvalia == '2':
                if not self.existe_avaliacao(cidade, usrlogado):
                    print("Voçê ainda nao avaliou esse ponto turistico!!")
                    return
                
                while True:
                    avaliacao = int( input("Informe uma nova nota entre (0-5): ") )
                    if avaliacao <= 0 or avaliacao > 5:
                        print("Informa um valor entre (0-5)")
                        continue
                    else:
                        break

                self.editar_avaliacao(usrlogado, cidade, avaliacao)
                break               

            elif opcMenuAvalia == '3':
                if not self.existe_avaliacao(cidade, usrlogado):
                    print("Voçê ainda nao avaliou esse ponto turistico!!")
                    return
                
                self.excluir_avaliacao(usrlogado, cidade)
                
                

            elif opcMenuAvalia == '0':
                break

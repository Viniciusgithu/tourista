from comandoarq import UsuariosModel #type: ignore
from usuario_interacao import UsuarioInterface

class GerenciadorArquivosController: # Criando a classe gerenciadora
    def __init__(self):
        self.model = UsuariosModel() # puxando classe do model e armazenando numa variável
        self.view = UsuarioInterface() # puxando classe do view e armazenando numa variável
    
    def login(self):
        while True:
            nome_usuario = self.view.entrada("nome do usuário: ")
            senha = self.view.entrada("Senha: ")

            for usuario in self.model.credenciais['usuarios']: # Procurar o usuário no arquivo json
                if usuario['nome_usuario'] == nome_usuario and usuario['senha'] == senha:
                    self.view.obter_mensagem("Login Efetuado!") # Achou o usuário e fez a verificação
                    return

            self.view.obter_mensagem("Login ou senha inválidos") # Não encontrado no arquivo json
            self.voltar_menu_opcao() # Função que chama a opção de retorno 

    def registrar(self):
        nome_usuario = self.view.entrada("Crie um nome de usuário: ") # Criação de nome do usuário
        if len(nome_usuario) <= 3: # Se o nome criado tenha 3 caracteres ou menos exibira tal mensagem:
            self.view.obter_mensagem("O usuário deve possuir no mínimo 4 caracteres.")
            self.registrar() # Irá retornar a função para criar outro nome, funcionando como um "loop"
        for usuario in self.model.credenciais['usuarios']: # Buscando o usuário no arquivo json
            if usuario['nome_usuario'] == nome_usuario: # Verificando caso exista o usuário no json
                self.view.obter_mensagem("Nome de usuário já existe")
                self.voltar_menu_opcao() # Chama a função de opção de voltar ao menu
                return self.registrar() # Caso for negada, ele irá voltar a função como um loop novamente
            
        while True:
            senha = self.view.entrada("Crie uma senha (No mínimo 8 caracteres e pelo menos um número): ")
            if len(senha) < 8: # Verificando se a senha criada tem mais do que 8 caracteres, caso não:
                self.view.obter_mensagem("A senha deve ter no mínimo 8 caracteres.")
            possui_numero = any(caractere.isdigit() for caractere in senha) # Variável booleana que verifica se na senha possui algum dígito
            
            if possui_numero == False: # caso não tenha:
                self.view.obter_mensagem("A senha deve ter pelo menos um dígito.")
                continue # Continuação do loop
            
            if len(senha) >= 8 and possui_numero == True: # Caso a senha seja aceita
                break # Quebrará o loop e pulará para o próximo escopo de código

        
        self.view.obter_mensagem("OBS: A palavra chave será seu acesso para quando esquecer a senha!")
        palavra_chave = self.view.entrada("Escolha uma palavra chave: ") # Usada para senha esquecida
        genero = self.view.entrada("Qual o seu gênero (0 - Masculino | 1 - Feminino  | 2 - Outro)? ") # Concedendo um gênero ao perfil, usado nas avaliações
        if genero == "0":
            palavra_genero = "Masculino" # Transformando o número entrado na palavra, para salvar no json
        elif genero == "1":
            palavra_genero = "Feminino"
        
        elif genero == "2":
            palavra_genero = "Outro"

        
        self.model.credenciais['usuarios'].append({"nome_usuario": nome_usuario, "senha": senha, "palavra_chave": palavra_chave, "genero": palavra_genero} )
        self.model.salvar_usuarios()
        self.view.obter_mensagem("Usuário registrado com sucesso!")
    
    def esqueci_senha(self):
        nome_usuario = self.view.entrada("nome do usuário: ")
        digitar_palavra_chave = self.view.entrada("Digite sua palavra chave: ")
        for usuario in self.model.credenciais['usuarios']:
            if usuario['palavra_chave'] == digitar_palavra_chave and nome_usuario == usuario['nome_usuario']:
                self.view.obter_mensagem("Palavra chave bem sucedida!")
                while True:
                    nova_senha = self.view.entrada("Digite sua nova senha: ")
                    confirmacao_senha = self.view.entrada("Confirme sua senha: ")
                    if nova_senha == confirmacao_senha:
                        usuario['senha'] = nova_senha
                        self.model.salvar_usuarios()
                        self.view.obter_mensagem("Senha alterada com sucesso")
                        return
                    
                    
                    else:
                        self.view.obter_mensagem("Senhas não compatíveis.")
                        self.view.obter_mensagem("")
                        self.voltar_menu_opcao()
                        self.alterar_senha(usuario)
                        
                    
        self.view.obter_mensagem("Nome de usuário ou palavra chave não encontrada.")

    def excluir_conta(self):
        nome_usuario = self.view.entrada("nome do usuário: ")
        senha = self.view.entrada("Digite sua senha: ")
        for usuario in self.model.credenciais['usuarios']:
            if usuario['nome_usuario'] == nome_usuario and usuario['senha'] == senha:
                 while True:
                    opcao = self.view.entrada(f"Você tem certeza que deseja excluir o turista {nome_usuario}? (Digite 'sim' ou 'nao'): ".lower().strip())
                    if opcao == 'sim':
                        self.model.credenciais['usuarios'].remove(usuario)
                        self.model.salvar_usuarios()
                        self.view.obter_mensagem("Turista removido com sucesso!")
                        return
                    elif opcao == 'nao':
                        self.view.obter_mensagem("Turista não removido")
                        return

                        
                    else: 
                        self.view.obter_mensagem("Digite apenas 'sim' ou 'nao'")
                
        self.view.obter_mensagem("Usuário ou senha incorreto(s)")

    
    def editar_usuario_menu(self):
        self.view.obter_mensagem("\nConfirme que é você:")
        nome_usuario = self.view.entrada("Nome do usuário: ")
        senha = self.view.entrada("Senha: ")
                
        for usuario in self.model.credenciais['usuarios']:
            if usuario['nome_usuario'] == nome_usuario and usuario['senha'] == senha:
                self.view.obter_mensagem("Usuário confirmado")
                print("")
                self.view.obter_mensagem("O que desejas alterar no perfil?\n1. Nome do usuário\n2. Senha\n3. Gênero")
                opcao = self.view.entrada("Digite uma opção: ")

                if opcao == '1':
                    self.alterar_nome(usuario)

                elif opcao == '2':
                    self.alterar_senha(usuario)
            
        self.view.obter_mensagem("Usuário não encontrado")
        self.voltar_menu_opcao()
        self.editar_usuario_menu()


    def alterar_nome(self, usuario):
            
            self.view.obter_mensagem("")
            novo_nome = self.view.entrada("Digite o novo nome do usuário: ")
            for turista in self.model.credenciais['usuarios']:
                    if turista['nome_usuario'] == novo_nome:
                        self.view.obter_mensagem("Nome de usuário já existe")
                        return self.alterar_nome(usuario)

            confirmar_nome = self.view.entrada("Confirme seu novo nome: ")
            if novo_nome == confirmar_nome:
                usuario['nome_usuario'] = novo_nome
                self.model.salvar_usuarios()
                self.view.obter_mensagem("Nome do usuário alterado com sucesso!")
                return self.menu()

            else:
                self.view.obter_mensagem("Nomes não compatíveis")
                self.voltar_menu_opcao()
                self.alterar_nome()
    
    def alterar_senha(self, usuario):
            
            self.view.obter_mensagem("")
            nova_senha = self.view.entrada("Digite sua nova senha: ")
            confirmar_senha = self.view.entrada("Confirme sua nova senha: ")
            if nova_senha == confirmar_senha:
                usuario['senha'] = nova_senha
                self.model.salvar_usuarios()
                self.view.obter_mensagem("Senha alterada com sucesso!")
                self.menu()
                
            
            else:
                self.view.obter_mensagem("Senhas não compatíveis")
                while True: 
                    self.voltar_menu_opcao()
                    self.alterar_senha(usuario)


    def menu(self):
        while True:
            self.view.obter_mensagem("----Bem vindo ao Tourista!!----")
            self.view.obter_mensagem("\n1. Login\n2. Registrar\n3. Esqueci a senha\n4. Excluir conta\n5. Editar o usuário")
            opcao = input("Digite uma opção: ")

            if opcao == '1':
                self.login()
            
            elif opcao == '2':
                self.registrar()
            
            elif opcao == '3':
                self.esqueci_senha()

            elif opcao == '4':
                self.excluir_conta()
            
            elif opcao == '5':
                self.editar_usuario_menu()

            else: 
                self.view.obter_mensagem("Digite uma das quatro opções")
    
    def voltar_menu_opcao(self):
    
        opcao = self.view.entrada("Deseja voltar a tela inicial ('s' para confirmar, 'n' para negar)? ").strip().lower()
        if opcao in ('s', 'sim'):
            self.menu()
        elif opcao in ('n', 'nao', 'não'):
            ...
        else:
            print("Opção inválida. Tente novamente.")


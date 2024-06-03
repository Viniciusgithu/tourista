from Model.dadosUsarios import UsuariosModel #type: ignore
from View.usuario_interacao import UsuarioInterface
from tour import executa

class GerenciadorArquivosController: # Criando a classe gerenciadora
    def __init__(self):
        self.model = UsuariosModel() # puxando classe do model e armazenando numa variável
        self.view = UsuarioInterface() # puxando classe do view e armazenando numa variável
    
    def login(self):
        while True:
            nome_usuario = self.view.entrada("Nome do Usuário: ")
            senha = self.view.entrada("Senha: ")

            for usuario in self.model.credenciais['usuarios']: # Procurar o usuário no arquivo json
                if usuario['nome_usuario'] == nome_usuario and usuario['senha'] == senha:
                    self.view.obter_mensagem("Login Efetuado!") # Achou o usuário e fez a verificação
                    return executa(nome_usuario)

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
        genero = self.view.entrada("Qual o seu gênero (0 - Masculino | 1 - Feminino  | 2 - Outros)? ") # Concedendo um gênero ao perfil, usado nas avaliações
        if genero == "0":
            palavra_genero = "Masculino" # Transformando o número entrado na palavra, para salvar no json
        elif genero == "1":
            palavra_genero = "Feminino"
        
        elif genero == "2":
            palavra_genero = "Outros"

        
        self.model.credenciais['usuarios'].append({"nome_usuario": nome_usuario, "senha": senha, "palavra_chave": palavra_chave, "genero": palavra_genero} ) # Adição de credenciais no json
        self.model.salvar_usuarios() # Salvar credenciais
        self.view.obter_mensagem("Usuário registrado com sucesso!")
    
    def esqueci_senha(self): # Opção de esquecer a senha:
        nome_usuario = self.view.entrada("nome do usuário: ")
        digitar_palavra_chave = self.view.entrada("Digite sua palavra chave: ") 
        for usuario in self.model.credenciais['usuarios']: # Rodar usuário por usuário no json
            if usuario['palavra_chave'] == digitar_palavra_chave and nome_usuario == usuario['nome_usuario']: # Verificar se o nome do usuário e a palavra chave se coincidem
                self.view.obter_mensagem("Palavra chave bem sucedida!")

                while True: # Entrar no escopo da alteração de senha depois da verificação:
                    nova_senha = self.view.entrada("Digite sua nova senha: ") # Nova senha
                    confirmacao_senha = self.view.entrada("Confirme sua senha: ") # Confirmação da senha
                    if nova_senha == confirmacao_senha:
                        usuario['senha'] = nova_senha # Se forem compatíveis, a senha do json irá ser substituída pela nova senha
                        self.model.salvar_usuarios() # Salvar credenciais
                        self.view.obter_mensagem("Senha alterada com sucesso")
                        return
                    
                    
                    else: # Caso a nova senha seria incompatível com a confirmação, executar este escopo:
                        self.view.obter_mensagem("Senhas não compatíveis.")
                        self.view.obter_mensagem("")
                        self.voltar_menu_opcao() # Opção de voltar ao menu
                        self.alterar_senha(usuario) # Caso rejeitada a opção irá retornar a função como um "loop"
                        
                    
        self.view.obter_mensagem("Nome de usuário ou palavra chave não encontrada.")
        self.voltar_menu_opcao()
        self.esqueci_senha

    def excluir_conta(self): # Função para excluir a conta:
        nome_usuario = self.view.entrada("nome do usuário: ")
        senha = self.view.entrada("Digite sua senha: ")
        for usuario in self.model.credenciais['usuarios']: # Buscar o usuário no arquivo json
            if usuario['nome_usuario'] == nome_usuario and usuario['senha'] == senha: # Caso ache:
                 while True:
                    opcao = self.view.entrada(f"Você tem certeza que deseja excluir o turista {nome_usuario}? (Digite 'sim' ou 'nao'): ") # Confirmação de exclusão
                    opcao_diminutivo = opcao.lower().strip() 
                    if opcao_diminutivo in ('sim', 's'): # Caso for permitido:
                        self.model.credenciais['usuarios'].remove(usuario) # Remove o usuario
                        self.model.salvar_usuarios() # Salva as alterações
                        self.view.obter_mensagem("Turista removido com sucesso!")
                        print("")
                        return
                    elif opcao_diminutivo in ('nao', 'n', "não"): # Caso for negado:
                        self.view.obter_mensagem("Turista não removido")
                        self.voltar_menu_opcao() # Opção de voltar ao menu
                        self.excluir_conta() # Caso rejeitado, retornar a função de excluir conta
                        return
                        
                    else:
                        self.view.obter_mensagem("Digite apenas 'sim' ou 'nao'") # Caso não digite o fornecido
                
        self.view.obter_mensagem("Usuário ou senha incorreto(s)") # Caso não ache o usuário no json
        self.voltar_menu_opcao() # Opção de voltar ao menu
        self.excluir_conta() # Caso rejeitado, retornará a função

    
    def editar_usuario_menu(self): # Opção de editar ao usuário:
        self.view.obter_mensagem("\nConfirme que é você:")
        nome_usuario = self.view.entrada("Nome do usuário: ")
        senha = self.view.entrada("Senha: ")
                
        for usuario in self.model.credenciais['usuarios']: # Procurar o usuário no arquivo json
            if usuario['nome_usuario'] == nome_usuario and usuario['senha'] == senha: # Confirmação do usuário:
                self.view.obter_mensagem("Usuário confirmado") 
                print("")
                while True:
                    self.view.obter_mensagem("O que desejas alterar no perfil?\n1. Nome do usuário\n2. Senha\n3. Gênero") # Opções que poderão ser alteradas
                    opcao = self.view.entrada("Digite uma opção: ")

                    if opcao == '1':
                        self.alterar_nome(usuario)

                    elif opcao == '2':
                        self.alterar_senha(usuario)
                    
                    elif opcao == '3':
                        self.alterar_genero(usuario)

                    else:
                        print("Digite de 1 a 3.")
                        self.voltar_menu_opcao()
                        continue

            
        self.view.obter_mensagem("Usuário não encontrado") # Caso o usuario ou senha não seja encontrada no json
        self.voltar_menu_opcao() # Opção de voltar ao menu
        self.editar_usuario_menu() # Caso rejeitada, voltará ao menu de edição do usuário


    def alterar_nome(self, usuario): # Função para alterar o nome, usado no menu de edição
            
            self.view.obter_mensagem("")
            novo_nome = self.view.entrada("Digite o novo nome do usuário: ") # Armazena o novo nome
            for turista in self.model.credenciais['usuarios']: # Busca usuário por usuário
                    if turista['nome_usuario'] == novo_nome: 
                        self.view.obter_mensagem("Nome de usuário já existe")
                        return self.alterar_nome(usuario) # Caso o nome já exista, retornará a função

            confirmar_nome = self.view.entrada("Confirme seu novo nome: ") # Confirma o novo nome
            if novo_nome == confirmar_nome: # Verifica se o nome digitado seja o mesmo da confirmação
                usuario['nome_usuario'] = novo_nome # Altera o nome do usuário no arquivo json
                self.model.salvar_usuarios() # Salva os dados no json
                self.view.obter_mensagem("Nome do usuário alterado com sucesso!")
                return self.menu() # Retorna ao menu

            else: # Entrará nesse escopo caso o usuário não seja encontrado no arquivo json
                self.view.obter_mensagem("Nomes não compatíveis")
                self.voltar_menu_opcao() # Opção de voltar ao menu
                self.alterar_nome(usuario) # Caso opção seja negada, retornará a função
    
    def alterar_senha(self, usuario): # Função de alterar senha para o menu de edição do usuário
            
            self.view.obter_mensagem("")
            nova_senha = self.view.entrada("Digite sua nova senha: ") # Digitar nova senha
            confirmar_senha = self.view.entrada("Confirme sua nova senha: ") # Confirmar a nova senha
            if nova_senha == confirmar_senha:
                usuario['senha'] = nova_senha # Caso a nova senha e a confirmação se coincide, altera a senha no arquivo json
                self.model.salvar_usuarios() # Salvar as alterações nas credenciais
                self.view.obter_mensagem("Senha alterada com sucesso!")
                self.menu() # Retorna ao menu
                
            
            else:
                self.view.obter_mensagem("Senhas não compatíveis") # Caso a senha não seja  a mesma 
                self.voltar_menu_opcao() # Opção de retornar ao menu
                self.alterar_senha(usuario) #Voltará a função de alterar senha
    
    def alterar_genero(self, usuario): # Função de alterar gênero no menu de edição de usuário
        self.view.obter_mensagem("")
        novo_genero = self.view.entrada("Qual o seu gênero (0 - Masculino | 1 - Feminino  | 2 - Outro)? ") # Opções de alteração de gênero
        if novo_genero == "0":
            palavra_genero = "Masculino" # Transformar a opção recebida em palavra para por no arquivo json
        elif novo_genero == "1":
            palavra_genero = "Feminino"
        
        elif novo_genero == "2":
            palavra_genero = "Outro"
        
        else: # Caso digite algo diferente do solicitado
            self.view.obter_mensagem("Digite apenas 0, 1 ou 2.")
            self.voltar_menu_opcao() # Opção de voltar ao menu
            self.alterar_genero(usuario) # Caso rejeitada, voltará a função de alterar gênero

        usuario['genero'] = palavra_genero # Alterará as novas credenciais
        self.model.salvar_usuarios() # Irá salvar as novas credenciais
        self.view.obter_mensagem("Gênero alterado com sucesso!")
        self.menu() # Voltará ao menu

    def menu(self): # Função do menu
        while True:
            self.view.obter_mensagem("---- ✈️ 🧳 Bem vindo ao Tourista ✈️ 🧳----")
            self.view.obter_mensagem("\n1. Login\n2. Registrar\n3. Esqueci a senha\n4. Excluir conta\n5. Editar o usuário") # Opções existentes da tela inicial
            print("")
            opcao = input("Digite uma opção: ")

            if opcao == '1':
                self.login() # Chamará função de login
            
            elif opcao == '2':
                self.registrar() # Chamará função de registro
            
            elif opcao == '3':
                self.esqueci_senha() # Chamará função de esqueci senha

            elif opcao == '4':
                self.excluir_conta() # Chamará função de exclusão de conta
            
            elif opcao == '5':
                self.editar_usuario_menu() # Chamará função de edição de usuário

            else: 
                self.view.obter_mensagem("Digite uma das quatro opções") # Caso for digitado algo difetente do solicitado
    
    def voltar_menu_opcao(self): # Função de voltar ao menu
        while True:
            opcao = self.view.entrada("Deseja voltar ao menu inicial ('s' para confirmar, 'n' para negar)? ").strip().lower() # Entrada se quer sair ou não, deixando a entrada minúscula e sem espaços
            if opcao in ('s', 'sim'):
                self.menu() # Caso queira sair, retorna ao menu inicial
            elif opcao in ('n', 'nao', 'não'):
                break # Caso não, quebra o loop e realizará a função fora dessa função
            else:
                print("Opção inválida. Tente novamente.") # Caso não digite o solicitado, irá retornar ao loop


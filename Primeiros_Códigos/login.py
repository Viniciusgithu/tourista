import hashlib

# Cria usuarios.txt e atribui um hash na sua senha


# Cadastro do usuário

#  1. Usuário deverá registrar a partir de: 
#   1.1 nome  (é o login)
#   1.2 sobrenome,
#   1.3 gênero
#   1.4 senha
#   1.5 Função esqueci senha

# Edição do perfil do usuário 
 

def carregar_usuarios():
    try:
        with open("usuarios.txt", "r") as file:
            users = {}
            for line in file:
                email, hashed_password = line.strip().split(",")
                users[email] = hashed_password
            return users
    except FileNotFoundError:
        return {}

def salvar_usuarios(users):
    with open("usuarios.txt", "w") as file:
        for email, hashed_password in users.items():
            file.write(f"{email},{hashed_password}\n")

def cadastrar_usuario(users):
    print("\nCadastro de novo usuário:")
    email = input("Digite seu email: ")
    if email in users:
        print("Este email já está cadastrado. Tente outro!")
        return
    password = input("Digite a senha: ")
    hashed_password = hashlib.sha256(password.encode()).hexdigest()
    users[email] = hashed_password
    salvar_usuarios(users)
    print("Usuário cadastrado com sucesso!")

def fazer_login(users):
    print("\nLogin:")
    email = input("Digite seu email: ")
    password = input("Digite a senha: ")
    hashed_password = hashlib.sha256(password.encode()).hexdigest()
    if users.get(email) == hashed_password:
        print("Login efetuado!")
    else:
        print("Email ou senha incorretos.")

def main():
    print("Bem-vindo ao Tourist!")
    users = carregar_usuarios()
    while True:
        print("\n1. Cadastrar novo usuário")
        print("2. Fazer login")
        print("3. Sair")
        opcao = input("Escolha uma opção (1,2,3) para prosseguir -> ")

        if opcao == '1':
            cadastrar_usuario(users)
        elif opcao == '2':
            fazer_login(users)
        elif opcao == '3':
            print("Saiu!")
            break
        else:
            print("Opção inválida! Tente novamente.")
            
            

if __name__ == "__main__":
    main()
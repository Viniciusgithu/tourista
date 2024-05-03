import pandas as pd

def main():
    print("")
    conta = input("Bem-vindo ao Tourista, Você já possui cadastro? ")
    if conta.lower() == "sim":
        print("Bem-vindo de volta! Por favor, faça login.")
        login_usuario()
    elif conta.lower() == "nao":
        print("Por favor, Cadastre-se abaixo.")
        cadastrar_usuario()
    else:
        print("Por favor, responda com (sim) ou (nao).")
def cadastrar_usuario():    
    nome = input("Digite seu nome: ")
    email = input("Digite seu email: ")
    senha = input("Digite sua senha: ")
    usuario = pd.DataFrame({'Nome': [nome], 'Senha': [senha], 'Email': [email]})
    usuario.to_csv('usuarios.csv', index=False)
    print("Parabéns! Voce criou sua conta.")
def login_usuario():
    email = input("Digite seu email: ")
    senha = input("Digite sua senha: ")
    try:
        usuarios = pd.read_csv('usuarios.csv')
        usuario = usuarios.loc[usuarios['Email'] == email]
        if not usuario.empty:
            if usuario['Senha'].iloc[0] == senha:
                print("Bem vindo de volta!")
            else:
                print("Senha incorreta. Tente novamente.")
        else:
            print("Nao foi possivel encontrar sua conta. Por favor, cadastre-se.")
            cadastrar_usuario()
    except FileNotFoundError:
        print("Por favor, cadastre-se.")
        cadastrar_usuario()
if __name__ == "__main__":
    main()

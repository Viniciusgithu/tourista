def mostrar_menu():
    print("Bem-vindo(a) ao Tourista!")
    print("Escolha uma opção:")
    print("1. Ver informações sobre um ponto turístico")
    print("2. Sair")

def mostrar_informacoes(ponto_turistico):
    print(f"Nome: {ponto_turistico['nome']}")
    print(f"Local: {ponto_turistico['local']}")
    print(f"Descrição: {ponto_turistico['descricao']}")
    print(f"Horário de Funcionamento: {ponto_turistico['horario_funcionamento']}")
    print(f"Custo de Entrada: {ponto_turistico['custo_entrada']}")
    print()

pontos_turisticos = {
    "Recife Antigo": {
        "nome": "Recife Antigo",
        "local": "Pernambuco - Brasil",
        "descricao": "Centro histórico com muitos bares e restaurantes.",
        "horario_funcionamento": "24 horas",
        "custo_entrada": "Gratuito"
    },
    "Parque das Ruínas": {
        "nome": "Parque das Ruínas",
        "local": "Pernambuco - Brasil",
        "descricao": "Parque com áreas verdes e ruínas históricas.",
        "horario_funcionamento": "9:00 - 17:00",
        "custo_entrada": "Gratuito"
    },
    "Parque da Jaqueira": {
        "nome": "Parque da Jaqueira",
        "local": "Pernambuco - Brasil",
        "descricao": "Parque arborizado com áreas para lazer e prática de esportes.",
        "horario_funcionamento": "5:00 - 22:00",
        "custo_entrada": "Gratuito"
    },
    "Museu Cais do Sertao": {
        "nome": "Museu Cais do Sertão",
        "local": "Pernambuco - Brasil",
        "descricao": "Museu dedicado à cultura nordestina, com exposições interativas.",
        "horario_funcionamento": "9:00 - 17:00",
        "custo_entrada": "R$ 10,00"
    },
    "Museu Ricardo Brennand": {
        "nome": "Museu Ricardo Brennand",
        "local": "Pernambuco - Brasil",
        "descricao": "Museu de arte com coleções de armas, armaduras e obras de arte.",
        "horario_funcionamento": "13:00 - 17:00 (fechado às segundas-feiras)",
        "custo_entrada": "R$ 20,00"
    },
    "Alto da Sé": {
        "nome": "Alto da Sé",
        "local": "Pernambuco - Brasil",
        "descricao": "Local histórico com uma vista panorâmica da cidade de Olinda.",
        "horario_funcionamento": "6h às 18h",
        "custo_entrada": "Gratuito"
    },
    "Machu Picchu": {
        "nome": "Machu Picchu",
        "local": "Peru",
        "descricao": "Antiga cidade inca no topo das montanhas dos Andes, no Peru.",
        "horario_funcionamento": "6h às 17h",
        "custo_entrada": "152 soles"
    },
    "Cristo Redentor": {
        "nome": "Cristo Redentor",
        "local": "Rio de Janeiro - Brasil",
        "descricao": "Estátua icônica de Jesus Cristo no topo do Morro do Corcovado, no Rio de Janeiro.",
        "horario_funcionamento": "8h às 19h",
        "custo_entrada": "R$26"
    },
    "Chichen Itza": {
        "nome": "Chichen Itza",
        "local": "México",
        "descricao": "Complexo de ruínas maias com uma grande pirâmide, no México.",
        "horario_funcionamento": "8h às 16h30",
        "custo_entrada": "480 pesos"
    },
    "Torre Eiffel": {
        "nome": "Torre Eiffel",
        "local": "Paris - França",
        "descricao": "Torre de ferro icônica localizada em Paris, na França.",
        "horario_funcionamento": "9h30 às 23h45",
        "custo_entrada": "€25,90"
    },
    "Coliseu": {
        "nome": "Coliseu",
        "local": "Roma - Itália",
        "descricao": "Anfiteatro antigo localizado em Roma, na Itália.",
        "horario_funcionamento": "8h30 às 19h",
        "custo_entrada": "€16"
    },
    "Palacio de Buckingham": {
        "nome": "Palácio de Buckingham",
        "local": "Londres - Inglaterra",
        "descricao": "Residência oficial da monarquia britânica em Londres, na Inglaterra.",
        "horario_funcionamento": "Varia",
        "custo_entrada": "Gratuito para visualização externa"
    },
    "Taj Mahal":{
        "nome": "Taj Mahal",
        "local": "Agra - Índia",
        "descricao": "É um mausoléu situado em Agra, na Índia, sendo o mais conhecido dos monumentos do país.",
        "horario_funcionamento": "abre 30 minutos antes do nascer do sol e fecha 30 minutos antes do por do sol”, e não funciona às sextas-feiras",
        "custo_entrada": "250 rupias"
    },
    "Estátua da Liberdade":{
        "nome": "Estátua da liberdade",
        "local": "Nova Iorque - EUA",
        "descricao": "é uma escultura neoclássica colossal localizada na ilha da Liberdade no porto de Nova Iorque, nos Estados Unidos.",
        "horario_funcionamento": "9h às 17h",
        "custo_entrada": "US$ 25,30"
    },
}

def main():
    while True:
        mostrar_menu()
        opcao = input("Escolha uma opção: ")
        
        if opcao == "1":
            ponto = input("Digite o nome do ponto turístico: ")
            if ponto in pontos_turisticos:
                mostrar_informacoes(pontos_turisticos[ponto])
            else:
                print("Ponto turístico não encontrado.")
        elif opcao == "2":
            print("Obrigado por usar o Tourista! Volte sempre!")
            break
        else:
            print("Opção inválida. Por favor, escolha uma opção válida.")

if __name__ == "__main__":
    main()

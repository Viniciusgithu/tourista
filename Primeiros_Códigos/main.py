pontos_turisticos = {
    "Recife": {
        "nome": "Recife Antigo",
        "descricao": "Centro histórico com muitos bares e restaurantes.",
        "horario_funcionamento": "24 horas",
        "custo_entrada": "Gratuito"
    },
    "Olinda": {
        "nome": "Alto da Sé",
        "descricao": "Local histórico com uma vista panorâmica da cidade.",
        "horario_funcionamento": "6h às 18h",
        "custo_entrada": "Gratuito"
    },
    "Peru": {
        "nome": "Machu Picchu",
        "descricao": "Antiga cidade inca no topo das montanhas dos Andes.",
        "horario_funcionamento": "6h às 17h",
        "custo_entrada": "152 soles"
    },
    "Rio de Janeiro": {
        "nome": "Cristo Redentor",
        "descricao": "Estátua icônica de Jesus Cristo no topo do Morro do Corcovado.",
        "horario_funcionamento": "8h às 19h",
        "custo_entrada": "R$26"
    },
    "México": {
        "nome": "Chichen Itza",
        "descricao": "Complexo de ruínas maias com uma grande pirâmide.",
        "horario_funcionamento": "8h às 16h30",
        "custo_entrada": "480 pesos"
    },
    "França": {
        "nome": "Torre Eiffel",
        "descricao": "Torre de ferro icônica localizada em Paris.",
        "horario_funcionamento": "9h30 às 23h45",
        "custo_entrada": "€25,90"
    },
    "Itália": {
        "nome": "Coliseu",
        "descricao": "Anfiteatro antigo localizado em Roma.",
        "horario_funcionamento": "8h30 às 19h",
        "custo_entrada": "€16"
    },
    "Inglaterra": {
        "nome": "Palácio de Buckingham",
        "descricao": "Residência oficial da monarquia britânica em Londres.",
        "horario_funcionamento": "Varia",
        "custo_entrada": "Gratuito para visualização externa"
    }
}


local = input("Digite um local: ")

if local in pontos_turisticos:
    ponto_turistico = pontos_turisticos[local]
    print(f"Nome: {ponto_turistico['nome']}")
    print(f"Descrição: {ponto_turistico['descricao']}")
    print(f"Horário de Funcionamento: {ponto_turistico['horario_funcionamento']}")
    print(f"Custo de Entrada: {ponto_turistico['custo_entrada']}")
else:
    print("Desculpe, não temos informações sobre este local.")

pontos_turisticos = {
    "Recife": {
        "nome": "Recife Antigo",
        "descricao": "Centro histórico com muitos bares e restaurantes.",
        "horario_funcionamento": "24 horas",
        "custo_entrada": "Gratuito"
        # avaliacao_do_visitante
        # imagem
        # restaurantes_famosos
        # monumentos
        # parques
    },
    "Olinda": {
        "nome": "Alto da Sé",
        "descricao": "Local histórico com uma vista panorâmica da cidade.",
        "horario_funcionamento": "6h às 18h",
        "custo_entrada": "Gratuito",
    
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

while True:
  #Adicionar imagem -> Pesquisar qual biblioteca usar (pillow) / usar o pyautogui para fechar a janela? 

  # Inicio do programa: 
    ##Menu inicial com recomendações dos pontos turísticos mais visitados (lembrar de exibir as avaliações de outros usuário)
    ###Deseja visitar algum desses? Indicar o pontos turísticos com as numerações: 1-2-3-4-5
    #Caso o usuário não queira visitar, iniciar a busca filtrada 
    #####Usário optou por saber mais: aparecerá informações detalhadas (página principal) sobre o lugar
    #####Após o usuário ler mostrar opção: avaliar, mais detalhes e sair do programa
    #####Caso o usário optar por mais detalhes: exibir mais informações sobre os tópicos
    #####Após os detalhes aparecerá as opções de voltar para o meu, avaliar e sair  
    

   #Após avaliar imprimir uma mensagem de sucesso e exibir o menu de busca

  print("\n*/*/*/*/* Bem vindo ao Tourista! */*/*/*/*\n")
  print("\n1. Pesquisar ponto turístico")
  print("\n----------------------------------------")
  print("\n2. Listar todos os pontos turísticos")
  print("\n----------------------------------------")
  print("\n3. Sair do Tourista")
  print("\n----------------------------------------")
  
#    Botar solicitação de avaliar
#    Pensar a forma de avaliação --> Ponto turístico/restaurante
   
  opcao = input("\nEscolha uma opção: ")


 
  if opcao == "1":
   local = input("Digite um local: ")
   if local in pontos_turisticos:
    ponto_turistico = pontos_turisticos[local]
    print(f"Nome: {ponto_turistico['nome']}")
    print(f"Descrição: {ponto_turistico['descricao']}")
    print(f"Horário de Funcionamento: {ponto_turistico['horario_funcionamento']}")
    print(f"Custo de Entrada: {ponto_turistico['custo_entrada']}")
    
   elif local not in pontos_turisticos:
    print("Desculpe, não temos informações sobre este local.\n Adicione um ponto turístico.")
    local_add = input("\nAdicione um novo local de ponto turístico: ")
    descricao_add = input("Digite a descrição do novo ponto turístico: ")
    horario_funcionamento_add = input("Digite o horário de funcionamento: ")
    custo_entrada_add = input("Digite o custo de entrada: ")

    pontos_turisticos[local] = {
            "nome": local_add,
            "descricao": descricao_add,
            "horario_funcionamento": horario_funcionamento_add,
            "custo_entrada": custo_entrada_add
        }
    print("\nPonto turístico adicionado com sucesso!")
    
  elif opcao == "2":
    
    for local, ponto_turistico in pontos_turisticos.items():
      
            print(f"\nLocal: {local}")
            print(f"Nome: {ponto_turistico['nome']}")
            print(f"Descrição: {ponto_turistico['descricao']}")
            print(f"Horário de Funcionamento: {ponto_turistico['horario_funcionamento']}")
            print(f"Custo de Entrada: {ponto_turistico['custo_entrada']}")
            
  elif opcao == "3":
        print("\n*/*/*/*/* O Tourista agradece a preferência, até a próxima! */*/*/*/*\n")
        break
      
  else:
        print("\nOpção inválida. Tente novamente.")

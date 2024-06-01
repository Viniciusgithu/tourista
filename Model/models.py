# model.py: Este é o arquivo onde você define suas classes de dados e funções relacionadas.

# Representa os dados e a lógica de negócios da aplicação; 
# Ele gerencia os dados;
# Implementa a lógica de negócios; 
# Interage com o banco de dados;
# Representa o estado atual da aplicação.
import json
import os

class PontoTuristico:
    def __init__(self, nome, local, descricao, horario_funcionamento, custo_entrada):
        self.nome = nome.lower()
        self.local = local
        self.descricao = descricao
        self.horario_funcionamento = horario_funcionamento
        self.custo_entrada = custo_entrada

class PontoTuristicoDAO:
    def __init__(self, arquivo_json):
        self.arquivo_json = arquivo_json

    def carregar_pontos_turisticos(self):
        try:
            with open(self.arquivo_json, 'r', encoding='utf-8') as f:
                dados = json.load(f)
                pontos_turisticos = []
                for ponto in dados["pontos_turisticos"]:
                    novo_ponto = PontoTuristico(
                        ponto["nome"],
                        ponto["local"],
                        ponto["descricao"],
                        ponto["horario_funcionamento"],
                        ponto["custo_entrada"]
                    )
                    pontos_turisticos.append(novo_ponto)
                return pontos_turisticos
        except FileNotFoundError:
            return []

    def adicionar_ponto_turistico(self, novo_ponto):
        pontos_turisticos = self.carregar_pontos_turisticos()
        pontos_turisticos.append(novo_ponto)
        self.salvar_pontos_turisticos(pontos_turisticos)

    def salvar_pontos_turisticos(self, pontos_turisticos):
        dados = {"pontos_turisticos": []}
        for ponto in pontos_turisticos:
            dados["pontos_turisticos"].append({
                "nome": ponto.nome,
                "local": ponto.local,
                "descricao": ponto.descricao,
                "horario_funcionamento": ponto.horario_funcionamento,
                "custo_entrada": ponto.custo_entrada
            })
        with open(self.arquivo_json, 'w', encoding='utf-8') as f:
            json.dump(dados, f, ensure_ascii=False, indent=4)

    def editar_ponto_turistico(self, ponto_atualizado):
        pontos_turisticos = self.carregar_pontos_turisticos()
        for i, ponto in enumerate(pontos_turisticos):
            if ponto.nome.lower() == ponto_atualizado.nome.lower():
                pontos_turisticos[i] = ponto_atualizado
                break
        self.salvar_pontos_turisticos(pontos_turisticos)

    def excluir_ponto_turistico(self, nome):
        pontos_turisticos = self.carregar_pontos_turisticos()
        pontos_turisticos = [ponto for ponto in pontos_turisticos if ponto.nome.lower() != nome.lower()]
        self.salvar_pontos_turisticos(pontos_turisticos)

class AvaliacoesUsuario:
    def __init__(self, nome_usuario, cidade, avaliacao):
        self.nome_usuario = nome_usuario.lower()
        self.cidade = cidade.lower()
        self.avaliacao = avaliacao

class AvaliacoesDAO:
    def __init__(self, file_path):
        self.file_path = file_path

    def load_json(self):
        if os.path.exists(self.file_path):
            with open(self.file_path, 'r') as file:
                return json.load(file)
        return []
    
    def salva_avaliacao(self, data):
        with open(self.file_path, 'w') as file:
            json.dump(data, file, indent=4)
    
    def adicionar_avaliacoes(self, nova_avaliacao):
        reviews = self.load_json()
        reviews.append({'usuario': nova_avaliacao.nome_usuario, 'cidade': nova_avaliacao.cidade, 'avaliacao': nova_avaliacao.avaliacao})
        self.salva_avaliacao(reviews)
        print("Avaliação salva com sucesso!!")

    def editar_avaliacoes(self, avaliacao):
        reviews = self.load_json()
        for review in reviews:
            if review['usuario'] == avaliacao.nome_usuario.lower() and review['cidade'] == avaliacao.cidade.lower():
                review['avaliacao'] = avaliacao.avaliacao
                self.salva_avaliacao(reviews)
                print("Avaliação salva com sucesso!!")
                return True  
        return False    

    def excluir_avaliacoes(self, avaliacao):
        reviews = self.load_json()
        updated_reviews = []
        for review in reviews:
            if not (review['usuario'] == avaliacao.nome_usuario.lower() and review['cidade'] == avaliacao.cidade.lower()):
                usr = review['usuario']
                cid =  review['cidade']
                ava = review['avaliacao']                
                updated_reviews.append({'usuario': usr, 'cidade': cid, 'avaliacao': ava})             
            
        self.salva_avaliacao(updated_reviews)
        print("Avaliação excluida com sucesso!!")
        return True

    # def read_reviews(self, cidade):
    #     reviews = self.load_json()
    #     return [review for review in reviews if review['ponto'] == cidade]

    # def delete_review(self, review_id):
    #     reviews = self.load_json()
    #     updated_reviews = [review for review in reviews if review['id'] != review_id]
    #     if len(reviews) == len(updated_reviews):
    #         return False
    #     else:
    #         self.save_json(updated_reviews)
    #         return True  
        
    def exibir_avaliacao(self, cidade):
        reviews = self.load_json()       
        
        # Filtrar os usuários que voltaram na cidade informada no paramentro
        cidade_users = [item for item in reviews if item["cidade"] == cidade]
        
        # Contar quantos usuários voltaram na cidade informada no paramentro
        num_cidade_users = len(cidade_users)        
       
        # Calcular a média aritmética das avaliações dos usuários que visitaram a cidade
        if num_cidade_users > 0:
            total_avaliacoes = sum(item["avaliacao"] for item in cidade_users)
            media_avaliacoes = total_avaliacoes / num_cidade_users
        else:
            media_avaliacoes = 0 

        if (num_cidade_users > 0):
            return (f"  O número de pessoas que avaliaram foram: {num_cidade_users}, e a avaliação está com uma média de {media_avaliacoes:.2f}")
        else:
           return (f"  A cidade {cidade} ainda não foi avalida.")        
        
           


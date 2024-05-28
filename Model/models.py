# model.py: Este é o arquivo onde você define suas classes de dados e funções relacionadas.

# Representa os dados e a lógica de negócios da aplicação; 
# Ele gerencia os dados;
# Implementa a lógica de negócios; 
# Interage com o banco de dados;
# Representa o estado atual da aplicação.
import json

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

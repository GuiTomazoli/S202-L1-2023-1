class QueryDatabase:
    def __init__(self, database):
        self.db = database

    def get_renzo(self):
        #Questão 1)a: Retorna o ano de nascimento e o cpf do professor com nome de Renzo do Database
        query = "MATCH (t:Teacher{name:'Renzo'}) RETURN t.ano_nasc, t.cpf"
        results = self.db.execute_query(query)
        return [(result["t.ano_nasc"], result["t.cpf"]) for result in results]
    
    def get_m(self):
        #Questão 1)b: Retorna os professores que começam com a letra M do Database
        query = "MATCH (t:Teacher) WHERE t.name STARTS WITH 'M' RETURN t.name, t.cpf"
        results = self.db.execute_query(query)
        return [(result["t.name"], result["t.cpf"]) for result in results]
    
    def get_city(self):
        #Questão 1)c: Retorna todos os nomes das cidades do Database
        query = "MATCH (c:City) WHERE c.name = 'Cidadezinha' OR c.name = 'Serra da Saudade' OR c.name = 'Santa Rita do SapucaÃ­' RETURN c.name"
        results = self.db.execute_query(query)
        return [result["c.name"] for result in results]
    
    def get_school(self):
        #Questão 1)d: Retorna todas as escolas onde o number seja maior ou igual a 150 e menor ou igual a 550 do Database
        query = "MATCH (s:School) WHERE s.number >= 150 AND s.number <= 550 RETURN s.name, s.address, s.number"
        results = self.db.execute_query(query)
        return [(result["s.name"], result["s.address"], result["s.number"]) for result in results]
    
    def get_nascimento(self):
        #Questão 2)a: Retorna o nascimento do professor mais velha e mais nova do Database
        query = "MATCH (t:Teacher) RETURN MIN(t.ano_nasc), MAX(t.ano_nasc)"
        results = self.db.execute_query(query)
        return [(result["MIN(t.ano_nasc)"], result["MAX(t.ano_nasc)"]) for result in results] 
    
    def get_media(self):
        #Questão 2)b: Retorna a média aritmética para os habitantes de todas as cidades do Database
        query = "MATCH (c:City) RETURN AVG(c.population)"
        results = self.db.execute_query(query)
        return [result["AVG(c.population)"] for result in results]
    
    def get_cep(self):
        #Questão 2)c: Retorna a cidade cujo CEP seja igual a “37540-000” e retorna o nome com todas as letras “a” substituídas por “A”  do Database
        query = "MATCH (c:City) WHERE c.cep = '37540-000' RETURN REPLACE(c.name, 'a', 'A')"
        results = self.db.execute_query(query)
        return [result["REPLACE(c.name, 'a', 'A')"] for result in results]
    
    def get_caractere(self):
        #Questão 2)d: Retorna um caractere, iniciando a partir da terceira letra do nome de todos os professores do Database
        query = "MATCH (t:Teacher) RETURN substring(t.name, 3, 1)"
        results = self.db.execute_query(query)
        return [result["substring(t.name, 3, 1)"]for result in results]
    
    

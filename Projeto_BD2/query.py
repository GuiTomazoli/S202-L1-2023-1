class QueryDatabase:
    def __init__(self, database):
        self.db = database

    #Relacionamentos
    def create_cadastro_medico(self, nome):
        #Faz o cadastro do medico no hospital
        query = "MATCH (h:Hospital {nome: $nome}),(m:Medico) CREATE (h)-[:TEM]->(m)"
        parameters = {"nome": nome}
        self.db.execute_query(query, parameters)

    def create_cadastro_paciente(self, nome):
        #Faz o cadastro do paciente no hospital
        query = "MATCH (h:Hospital {nome: $nome}),(p:Paciente) CREATE (h)-[:TEM]->(p)"
        parameters = {"nome": nome}
        self.db.execute_query(query, parameters)

    def create_consulta(self, nome_paciente, nome_medico):
        #Faz uma consulta do paciente para o medico
        query = "MATCH (p:Paciente {nome: $nome_paciente}),(m:Medico {nome: $nome_medico}) CREATE (p)-[:TEM_CONSULTA]->(m)"
        parameters = {"nome_paciente": nome_paciente, "nome_medico": nome_medico}
        self.db.execute_query(query, parameters)

    #Gets
    def get_hospital(self):
        query = "MATCH (h:Hospital) RETURN h"
        results = self.db.execute_query(query)
        return [result["h"] for result in results]
    
    def get_medicos(self):
        query = "MATCH (m:Medico) RETURN m"
        results = self.db.execute_query(query)
        return [result["m"] for result in results]
    
    def get_pacientes(self):
        query = "MATCH (p:Paciente) RETURN p"
        results = self.db.execute_query(query)
        return [result["p"] for result in results]
    
    
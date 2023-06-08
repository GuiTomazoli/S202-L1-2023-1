from Hospital import Hospital
from Medico import Medico
from Paciente import Paciente

class HospitalCRUDDatabase:
    def __init__(self, database):
        self.db = database

    #Criar Hospital
    def create_hospital(self, hospital:Hospital):
        query = "CREATE (:Hospital {nome: $nome, localizacao: $localizacao})"
        parameters = {"nome": hospital.nome, "localizacao": hospital.localizacao}
        self.db.execute_query(query, parameters)

    #CRUD Medico
    def create_medico(self, Medicos:Medico):
        query = "CREATE (:Medico {nome: $nome, idade: $idade, crm: $crm, especialidade: $especialidade})"
        parameters = {"nome": Medicos.nome, "idade": Medicos.idade, "crm": Medicos.crm, "especialidade": Medicos.especialidade}
        self.db.execute_query(query, parameters)
    
    def read_medico(self, nome):
        query = "MATCH (m:Medico {nome: $nome}) RETURN m"
        parameters = {"nome": nome}
        results = self.db.execute_query(query, parameters)
        return [result["m"] for result in results]
    
    def update_medico(self, nome, nova_idade, novo_crm, nova_especialidade ):
        query = "MATCH (m:Medico {nome: $nome}) SET m.idade = $nova_idade, m.crm = $novo_crm, m.especialidade = $nova_especialidade"
        parameters = {"nome": nome, "nova_idade": nova_idade, "novo_crm": novo_crm, "nova_especialidade": nova_especialidade}
        self.db.execute_query(query, parameters)

    def delete_medico(self, nome):
        query = "MATCH (m:Medico {nome: $nome}) DETACH DELETE m"
        parameters = {"nome": nome}
        self.db.execute_query(query, parameters)

    #CRUD Paciente
    def create_paciente(self, Pacientes:Paciente):
        query = "CREATE (:Paciente {nome: $nome, idade: $idade, cpf: $cpf})"
        parameters = {"nome": Pacientes.nome, "idade": Pacientes.idade, "cpf": Pacientes.cpf}
        self.db.execute_query(query, parameters)
    
    def read_paciente(self, nome):
        query = "MATCH (p:Paciente {nome: $nome}) RETURN p"
        parameters = {"nome": nome}
        results = self.db.execute_query(query, parameters)
        return [result["p"] for result in results]

    def update_paciente(self, nome, nova_idade, novo_cpf ):
        query = "MATCH (p:Paciente {nome: $nome}) SET p.idade = $nova_idade, p.cpf = $novo_cpf"
        parameters = {"nome": nome, "nova_idade": nova_idade, "novo_cpf": novo_cpf}
        self.db.execute_query(query, parameters)

    def delete_paciente(self, nome):
        query = "MATCH (p:Paciente {nome: $nome}) DETACH DELETE p"
        parameters = {"nome": nome}
        self.db.execute_query(query, parameters)





    

    

    


    

    
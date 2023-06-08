from database import Database
from Hospital import Hospital
from Medico import Medico
from Paciente import Paciente
from hospital_crud import HospitalCRUDDatabase
from query import QueryDatabase
from cli import HospitalCLI

# Cria uma instância da classe Database, passando os dados de conexão com o banco de dados Neo4j
db = Database("bolt://3.239.228.39:7687", "neo4j", "acronyms-pass-administrators")
#db.drop_all()

# Criando uma instância da classe Hospital_CRUD para interagir com o banco de dados
hospital_crud_db = HospitalCRUDDatabase(db)
# Criando uma instância da classe Query para interagir com o banco de dados
query_db = QueryDatabase(db)

#Criando um Hospital
print("\n")
hospital = Hospital("Albert Einsten", "Sao Paulo")
hospital_crud_db.create_hospital(hospital)

#CRUD Medicos
medico = Medico("João", 45, 123, "Medico Geral")
hospital_crud_db.create_medico(medico)
print("Medico:")
print(hospital_crud_db.read_medico("João"))
hospital_crud_db.update_medico("João", 50, 159, "Oftalmologista")
hospital_crud_db.delete_medico("João")
print("\n")

#CRUD Pacientes
paciente = Paciente("Guilherme", 22, "123456789")
hospital_crud_db.create_paciente(paciente)
print("Paciente:")
print(hospital_crud_db.read_paciente("Guilherme"))
hospital_crud_db.update_paciente("Guilherme", 23, "149.520.796-00")
hospital_crud_db.delete_paciente("Guilherme")
print("\n")

#Relacionamentos
query_db.create_cadastro_medico("Albert Einsten")
query_db.create_cadastro_paciente("Albert Einsten")
query_db.create_consulta("João", "Luis")

# Imprimindo todas as informações do banco de dados
print("Hospital:")
print(query_db.get_hospital())
print("\n")
print("Medicos:")
print(query_db.get_medicos())
print("\n")
print("Pacientes:")
print(query_db.get_pacientes())
print("\n")

#CLI
HospitalModel = HospitalCRUDDatabase(database=db)
HospitalCLI = HospitalCLI(HospitalModel)
HospitalCLI.run()

# Fechando a conexão com o banco de dados
db.close()
from database import Database
from query import QueryDatabase
from teacher_crud import TeacherCRUDDatabase
from cli import TeacherCLI

# cria uma instância da classe Database, passando os dados de conexão com o banco de dados Neo4j
db = Database("bolt://3.93.9.108:7687", "neo4j", "boards-subject-ration")

# Criando uma instância da classe Query para interagir com o banco de dados
query_db = QueryDatabase(db)
# Criando uma instância da classe Teacher_CRUD para interagir com o banco de dados
teacher_crud_db = TeacherCRUDDatabase(db)

# Imprimindo todas as informações da Questão 1) do banco de dados
print("Questão 1)a:")
print("Professores com o nome Renzo do Database:")
print(query_db.get_renzo())
print("\n")
print("Questão 1)b:")
print("Professores que começam com a letra M do Database:")
print(query_db.get_m())
print("\n")
print("Questão 1)c:")
print("Nome das cidades do Database:")
print(query_db.get_city())
print("\n")
print("Questão 1)d:")
print("Escolas com o numero maior ou igual á 150 e menor ou igual a 550:")
print(query_db.get_school())
print("\n")

# Imprimindo todas as informações da Questão 2) do banco de dados
print("Questão 2)a:")
print("O ano de nascimento do professor mais jovem e do mais velho:")
print(query_db.get_nascimento())
print("\n")
print("Questão 2)b:")
print("Media das populações das cidades:")
print(query_db.get_media())
print("\n")
print("Questão 2)c:")
print("A cidade com o CEP 37540-00 e as letras 'as' de seu nome para letras maiusculas:")
print(query_db.get_cep())
print("\n")
print("Questão 2)d:")
print("O caractere iniciado a partir da terceira letra do nome de todos os professores:")
print(query_db.get_caractere())
print("\n")

# Imprimindo todas as informações da Questão 3) do banco de dados
#Questão 3)b
teacher_crud_db.create_teacher("Chris Lima", 1956, "189.052.396-66")
print("Questão 3)c:")
print("Professores com o nome Chris Lima do Database:")
print(teacher_crud_db.read_teacher("Chris Lima"))
print("\n")
#Questão 3)d
teacher_crud_db.update_teacher("Chris Lima", "162.052.777-77")
#Questão 3)e
TeacherModel = TeacherCRUDDatabase(database=db)
teacherCLI = TeacherCLI(TeacherModel)
teacherCLI.run()

# Fechando a conexão com o banco de dados
db.close()
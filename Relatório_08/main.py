from database import Database
from school_database import SchoolDatabase
#from game_database import GameDatabase

# cria uma instância da classe Database, passando os dados de conexão com o banco de dados Neo4j
db = Database("bolt://34.200.223.91:7687", "neo4j", "exhaust-soil-introductions")
db.drop_all()

# Criando uma instância da classe SchoolDatabase para interagir com o banco de dados
school_db = SchoolDatabase(db)
# Criando uma instância da classe Game_Database para interagir com o banco de dados
#game_db = GameDatabase(db)

# Criando alguns professores
school_db.create_professor("João")
school_db.create_professor("Maria")
school_db.create_professor("José")
# Criando alguns players
#game_db.create_player("João", 1)
#game_db.create_player("Maria", 2)
#game_db.create_player("José", 3)

# Criando alguns alunos
school_db.create_aluno("Ana")
school_db.create_aluno("Carlos")
school_db.create_aluno("Beatriz")
# Criando uma match
#game_db.create_match("Partida1", 1, "Jogadores: Pedro, Maria", "Vencedor: Maria")
#game_db.create_match("Partida2", 2, "Jogadores: Maria, José", "Vencedor: José")
#game_db.create_match("Partida3", 3, "Jogadores: Pedro, José", "Vencedor: Pedro")

# Criando algumas aulas e suas relações com os professores
school_db.create_aula("Matemática", "João")
school_db.create_aula("Português", "Maria")
school_db.create_aula("História", "José")
# Criando um jogo e suas relações com os players
#game_db.create_game("Fortnite", "João")
#game_db.create_game("Call of Duty Warzone", "Maria")
#game_db.create_game("Apex Legends", "José")

# Atualizando o nome de um professor
school_db.update_professor("João", "Pedro")
# Atualizando o nome de um player
#game_db.update_player("João", "Pedro")

school_db.insert_aluno_aula("Ana", "Matemática")
school_db.insert_aluno_aula("Ana", "Português")
school_db.insert_aluno_aula("Carlos", "História")
school_db.insert_aluno_aula("Beatriz", "História")
#game_db.insert_match_game("Partida1", "Fortnite")
#game_db.insert_match_game("Partida2", "Call of Duty Warzone")
#game_db.insert_match_game("Partida3", "Apex Legends")

school_db.insert_professor_aula("Maria", "Matemática")
school_db.insert_professor_aula("José", "Português")
school_db.insert_professor_aula("José", "Matemática")
#game_db.insert_player_game("Maria", "Fortnite")
#game_db.insert_player_game("José", "Call of Duty Warzone")
#game_db.insert_player_game("Pedro", "Apex Legends")


# Imprimindo todas as informações do banco de dados
print("Professores:")
print(school_db.get_professores())
print("Alunos:")
print(school_db.get_alunos())
print("Aulas:")
print(school_db.get_aulas())

# Imprimindo todas as informações do banco de dados
#print("Players:")
#print(game_db.get_players())
#print("Matches:")
#print(game_db.get_matches())
#print("Games:")
#print(game_db.get_games())

# Fechando a conexão com o banco de dados
db.close()
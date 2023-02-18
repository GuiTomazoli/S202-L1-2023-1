assunto = "POO"

class Professor:
    def __init__(self, nome):
        self.nome = nome

    def ministrar_aula(self):
        print(f'O professor {self.nome} está ministrando uma aula sobre {assunto}')

chris = Professor('Chris')
chris.ministrar_aula()

class Aluno:
    def __init__(self, nome):
        self.nome = nome

    def presenca(self):
        print(f'O aluno {self.nome} está presente')

guilherme = Aluno('Guilherme')
guilherme.presenca()

class Aula:
    def __init__(self, professor, assunto):
        self.professor = professor
        self.assunto = assunto
        self.alunos = []

    def adicionar_aluno(self,aluno):
        self.alunos.append(aluno)

   
    def listar_presenca(self):
        print(f'Presença na aula sobre {self.assunto}, ministrada pelo professor {self.professor}') 
        for aluno in self.alunos:
            print('Alunos:' + aluno.nome)

pedro = Aluno('Pedro')
lucas = Aluno('Lucas')
diego = Aluno('Diego')

POO = Aula('Chris', 'POO')
POO.adicionar_aluno(guilherme)
POO.adicionar_aluno(pedro)
POO.adicionar_aluno(lucas)
POO.adicionar_aluno(diego)

POO.listar_presenca()












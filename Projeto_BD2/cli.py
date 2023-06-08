from Paciente import Paciente
from Medico import Medico

class SimpleCLI:
    def __init__(self):
        self.commands = {}

    def add_command(self, nome, function):
        self.commands[nome] = function

    def run(self):
        while True:
            command = input("Enter a command: ")
            if command == "quit":
                print("Goodbye!")
                break
            elif command in self.commands:
                self.commands[command]()
            else:
                print("Invalid command. Try again.")


class HospitalCLI(SimpleCLI):
    def __init__(self, hospital_model):
        super().__init__()
        self.hospital_model = hospital_model
        self.add_command("create_medico", self.create_medico)
        self.add_command("read_medico", self.read_medico)
        self.add_command("update_medico", self.update_medico)
        self.add_command("delete_medico", self.delete_medico)
        self.add_command("create_paciente", self.create_paciente)
        self.add_command("read_paciente", self.read_paciente)
        self.add_command("update_paciente", self.update_paciente)
        self.add_command("delete_paciente", self.delete_paciente)

    #CLI Medico
    def create_medico(self):
        nome = input("Entre com o nome do medico: ")
        idade = int(input("Entre com a idade do medico: "))
        crm = int(input("Entre com o crm do medico: "))
        especialidade = input("Entre com a especialidade do medico: ")
        Medicos = Medico(nome, idade, crm, especialidade)
        if idade >= 23 and idade <= 80 and crm >= 0:
            self.hospital_model.create_medico(Medicos)
            print("***Medico criado com sucesso***")
        else:
            print("Algum valor invalido, criar de novo um medico")

    def read_medico(self):
        nome = input("Entre com o nome do medico que deseja ler: ")
        medico = self.hospital_model.read_medico(nome)
        if medico:
            medico = medico[0]
            print(f"Nome do medico: {medico['nome']}")
            print(f"Idade do medico: {medico['idade']}")
            print(f"CRM do medico: {medico['crm']}")
            print(f"Especialidade do medico: {medico['especialidade']}")

    def update_medico(self):
        nome = input("Entre com o nome do medico que deseja atualizar: ")
        idade = int(input("Entre com a nova idade do medico: "))
        crm = int(input("Entre com o novo crm do medico: "))
        especialidade = input("Entre com a nova especialidade do medico: ")
        if idade >= 23 and idade <= 80 and crm >= 0:
            self.hospital_model.update_medico(nome, idade, crm, especialidade)
            print("***Medico atualizado com sucesso***")
        else:
            print("Algum valor invalido, atualizar de novo o medico")

    def delete_medico(self):
        nome = input("Digite o nome do medico que deseja excluir: ")
        self.hospital_model.delete_medico(nome)
        print("***Medico deletado com sucesso***")

    #CLI Paciente
    def create_paciente(self):
        nome = input("Entre com o nome do paciente: ")
        idade = int(input("Entre com a idade do paciente: "))
        cpf = input("Entre com o cpf do paciente: ")
        Pacientes = Paciente(nome, idade, cpf)
        if idade > 0 and idade <= 150:
            self.hospital_model.create_paciente(Pacientes)
            print("***Paciente criado com sucesso***")
        else:
            print("Algum valor invalido, criar de novo um paciente")

    def read_paciente(self):
        nome = input("Entre com o nome do paciente que deseja ler: ")
        paciente = self.hospital_model.read_paciente(nome)
        if paciente:
            paciente = paciente[0]
            print(f"Nome do paciente: {paciente['nome']}")
            print(f"Idade do paciente: {paciente['idade']}")
            print(f"CPF do paciente: {paciente['cpf']}")

    def update_paciente(self):
        nome = input("Entre com o nome do paciente que deseja atualizar: ")
        idade = int(input("Entre com a nova idade do paciente: "))
        cpf = input("Entre com o novo cpf do paciente: ")
        if idade > 0 and idade <= 150:
            self.hospital_model.update_paciente(nome, idade, cpf)
            print("***Paciente atualizado com sucesso***")
        else:
            print("Algum valor invalido, atualizar de novo o paciente")

    def delete_paciente(self):
        nome = input("Digite o nome do paciente que deseja excluir: ")
        self.hospital_model.delete_paciente(nome)
        print("***Paciente deletado com sucesso***")
    
    def run(self):
        print("Welcome to the hospital, CLI!")
        print("Available commands: create_medico, read_medico, update_medico, delete_medico, create_paciente, read_paciente, update_paciente, delete_paciente, quit")
        super().run()
from Corrida import Corrida
from Passageiro import Passageiro
from MotoristaDAO import motoristaModel
from Motorista import Motorista

class SimpleCLI:
    def __init__(self):
        self.commands = {}

    def add_command(self, notaMotorista, function):
        self.commands[notaMotorista] = function

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


class motoristaCLI(SimpleCLI):
    def __init__(self, motorista_model):
        super().__init__()
        self.motorista_model = motorista_model
        self.add_command("create_motorista", self.create_motorista)
        self.add_command("read_motorista", self.read_motorista)
        self.add_command("update_motorista", self.update_motorista)
        self.add_command("delete_motorista", self.delete_motorista)

    def create_motorista(self):
        nome = input("Crie um nome para o passageiro: ")
        documento = input("Crie um documento para o passageiro: ")
        Passageiros = Passageiro(nome, documento)
        corridas = []
        while True:
            nota =  int(input("Crie uma nota para a corrida de  0 a 10: "))
            distancia =  float(input("Crie uma distancia para a corrida de > 0: "))
            valor =  float(input("Crie um valor para a corrida de >= 0: "))
            Corridas = Corrida(nota, distancia, valor, Passageiros)
            corridas.append(Corridas.__dict__)
            nota =  int(input("Crie uma nota para o motorista de  0 a 10: "))
            motorista = Motorista(corridas, nota)
            if nota >= 0 and nota <= 10 and distancia > 0 and valor >= 0:
                self.motorista_model.create_motorista(motorista, Corridas, Passageiros)
            else:
                print("Algum valor invalido, criar novo motorista")

            opcao = input("Deseja adicionar mais uma corrida? (S/N): ")
            if opcao == "N":
                break

    def read_motorista(self):
        id = input("Entre com o id: ")
        motorista = self.motorista_model.read_motorista_by_id(id)
        if motorista:
            print(f"Nome do Passageiro: {motorista['nome']}")
            print(f"Documento do Passageiro: {motorista['documento']}")
            print(f"Nota da Corrida: {motorista['nota']}")
            print(f"Distancia da Corrida: {motorista['distancia']}")
            print(f"Valor da Corrida: {motorista['valor']}")

    def update_motorista(self):
        id = input("Enter the id: ")
        nome = input("Crie um novo nome para o passageiro: ")
        documento = input("Crie um novo documento para o passageiro: ")
        Passageiros = Passageiro(nome, documento)
        corridas = []
        nota = int(input("Crie uma nova nota para a corrida de 0 a 10: "))
        distancia =  float(input("Crie uma nova distancia para a corrida de > 0: "))
        valor =  float(input("Crie um novo valor para a corrida de >= 0: "))
        Corridas = Corrida(nota, distancia, valor, Passageiros)
        corridas.append(Corridas.__dict__)
        nota = int(input("Crie uma nova nota para o motorista de 0 a 10: "))
        motorista = Motorista(corridas, nota)
        if nota >= 0 and nota <= 10 and distancia > 0 and valor >= 0:
            self.motorista_model.update_motorista(id, motorista, Corridas, Passageiros)
        else:
            print("Algum valor invalido, atualizar de novo o motorista")

    def delete_motorista(self):
        id = input("Entre com o id: ")
        self.motorista_model.delete_motorista(id)

    def run(self):
        print("Welcome to the Motorista CLI!")
        print("Available commands: create_motorista, read_motorista, update_motorista, delete_motorista, quit")
        super().run()
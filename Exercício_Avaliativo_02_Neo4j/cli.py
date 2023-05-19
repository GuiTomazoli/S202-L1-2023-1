class SimpleCLI:
    def __init__(self):
        self.commands = {}

    def add_command(self, name, function):
        self.commands[name] = function

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


class TeacherCLI(SimpleCLI):
    def __init__(self, teacher_model):
        super().__init__()
        self.teacher_model = teacher_model
        self.add_command("create", self.create_teacher)
        self.add_command("read", self.read_teacher)
        self.add_command("update", self.update_teacher)
        self.add_command("delete", self.delete_teacher)

    def create_teacher(self):
        name = input("Entre com o nome do professor: ")
        ano_nasc = int(input("Entre com o ano de nascimento do professor: "))
        cpf = input("Entre com o cpf do professor: ")
        self.teacher_model.create_teacher(name, ano_nasc, cpf)

    def read_teacher(self):
        name = input("Entre com o nome  do professor que deseja ler: ")
        teacher = self.teacher_model.read_teacher(name)
        if teacher:
            teacher = teacher[0]
            print(f"Nome do professor: {teacher['name']}")
            print(f"Ano de nascimento do professor: {teacher['ano_nasc']}")
            print(f"CPF do professor: {teacher['cpf']}")

    def update_teacher(self):
        name = input("Entre com o nome do professor que deseja atualizar: ")
        cpf = input("Entre com o novo cpf do professor: ")

        self.teacher_model.update_teacher(name, cpf)

    def delete_teacher(self):
        name = input("Digite o nome do professor que deseja excluir: ")
        self.teacher_model.delete_teacher(name)
        
    def run(self):
        print("Welcome to the teacher CLI!")
        print("Available commands: create, read, update, delete, quit")
        super().run()
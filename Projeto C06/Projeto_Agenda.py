from abc import ABC, abstractmethod  #biblioteca para trabalhar com classes abstratas, classa abstrata não pode ser instanciada diretamente 

class Pessoa(ABC):
    def __init__(self, nome):
        self.nome = nome

    @abstractmethod
    def get_contato(self):
        pass

class Contato(Pessoa):
    def __init__(self, nome, telefone, email):
        super().__init__(nome)
        self.telefone = telefone
        self.email = email

    def get_contato(self):
        return f"Nome: {self.nome}, Telefone: {self.telefone}, Email: {self.email}"

    def __str__(self):
        return self.get_contato()

class Agenda:
    def __init__(self):
        self.contatos = []

    def adicionar_contato(self, contato):
        if not isinstance(contato, Contato):  #verifica se o contato pertence a classe Contato
            raise TypeError("O contato fornecido não é um contato válido.")
        self.contatos.append(contato)

    def remover_contato(self, nome):
        for contato in self.contatos:
            if contato.nome == nome:
                self.contatos.remove(contato)
                return True
        return False

    def buscar_contato(self, nome):
        for contato in self.contatos:
            if contato.nome == nome:
                return contato
        return None

    def listar_contatos(self):
        return self.contatos

def menu():
    agenda = Agenda()
    while True:
        print("\n-------AGENDA DE CONTATOS------")
        print("\n1. Adicionar Contato")
        print("2. Remover Contato")
        print("3. Listar Contatos")
        print("4. Buscar Contato")
        print("5. Sair")

        escolha = input("Digite a opção desejada:")

        if escolha == "1":
            try:
                nome = input("Digite o nome do contato:").strip() #strip() é usado para remover espaços em branco
                telefone = input("Digite o telefone do contato:").strip()
                email = input("Digite o email do contato:").strip()

                if not nome or not telefone or not email:
                    raise ValueError("Todos os campos são obrigatórios!")

                novo_contato = Contato(nome, telefone, email)
                agenda.adicionar_contato(novo_contato)
                print(f"Contato {nome} adicionado com sucesso!")
            except Exception as e:
                print(f"Erro ao adicionar contato: {e}")

        elif escolha == "2":
            nome = input("Digite o nome do contato que deseja remover:").strip()
            if agenda.remover_contato(nome):
                print("Contato removido com sucesso")
            else:
                print("Contato não encontrado")

        elif escolha == "3":
            print("Listando todos os contatos:")
            for contato in agenda.listar_contatos():
                print(contato)

        elif escolha == "4":
            nome = input("Digite o nome do contato a ser buscado:").strip()
            contato = agenda.buscar_contato(nome)
            if contato:
                print(contato)
            else:
                print("Contato não encontrado")

        elif escolha == "5":
            print("Saindo do programa...")
            break
        else:
            print("Opção Inválida")
if __name__ == "__main__":
    menu()

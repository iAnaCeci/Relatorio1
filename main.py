class Professor:
    def __init__(self, nome, assunto):
        self.nome = nome
        self.assunto = assunto

    def ministrar_aula(self):
        print(f'O professor {self.nome} está ministrando uma aula sobre {self.assunto}!')

joao = Professor("Joao","Matematica")
joao.ministrar_aula()


class Aluna:
    def __init__(self, nome):
        self.nome = nome

    def presenca(self):
        print(f"O aluno(a) {self.nome}, está presente")


ana = Aluna("Ana")
ana.presenca()


class Aula:
    def __init__(self, professor, assunto, alunos):
        self.professor = professor
        self.assuntos = assunto
        self.alunos = alunos

    def adicionar_alunos(self,aluno):
        self.alunos.append(aluno)

    def listar_presenca(self):
        print(f"Presença na aula sobre {self.assuntos}, ministrada pelo professor {self.professor}"," estava presentes: " "{self.alunos}:")

list1 = []
aula = Aula("Marcos", "POO", list1)
aula.adicionar_alunos("Maria")
aula.adicionar_alunos("Joa0")
aula.listar_presenca()
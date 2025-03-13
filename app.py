class Curso:
    def __init__(self, nome_curso, materias, quant_aulas, quant_alunos):
        self._nome_curso = nome_curso # protegido
        self._materias = materias  # protegido
        self.__quant_aulas = int(quant_aulas)  # privado
        self.__quant_alunos = int(quant_alunos)  # privado


    # visibilidade privada (__) ou protegida (_).

    # Métodos GET
    def get_nome_curso(self):
        return self._nome_curso

    def get_materias(self):
        return self._materias

    def get_quant_aulas(self):
        return self.__quant_aulas

    def get_quant_alunos(self):
        return self.__quant_alunos



    # Métodos SET
    def set_quant_aulas(self, valor):
        if valor >= 0:
            self.__quant_aulas = valor
        else:
            print('Quantidade de aulas inválida.')

    def set_quant_alunos(self, valor):
        if valor >= 0:
            self.__quant_alunos = valor
        else:
            print('Quantidade de alunos inválida.')



    # GET voce recebe informação, SET é para mandar informação

    def apresentar(self):
        print("+", "-" * 30, "+")
        print(f"Olá, sou aluno(a) do curso: {self.get_nome_curso()},\n"
              f"Minha matéria favorita é: {self.get_materias()},\n"
              f"Tenho {self.get_quant_aulas()} aulas semanais,\n"
              f"E meu curso tem {self.get_quant_alunos()} alunos. Situação atual:")
        print("-" * 20)

        if self.__quant_alunos == 0:
            print('O curso não teve nenhuma matrícula realizada no mês.')
        elif self.__quant_alunos <= 10:
            print(
                f'O curso está começando a receber mensalidades. Atualmente, temos {self.get_quant_alunos()} alunos pagantes.')
        elif 10 < self.__quant_alunos <= 50:
            print(f'O curso está bastante popular! Atualmente, temos {self.get_quant_alunos()} alunos pagantes.')
        else:
            print(f'O curso está muito popular! Temos {self.get_quant_alunos()} alunos pagantes.')

    def matriculas(self):
        if self.__quant_alunos == 0:
            print('Nenhuma matrícula foi realizada ainda.')
        elif self.__quant_alunos <= 10:
            print('Poucos alunos, mas é um bom começo.')
        elif 10 < self.__quant_alunos <= 50:
            print('Bastantes alunos no curso, muito bom!')
        else:
            print(f'Muitos alunos no cursos, está ótimo suas matrículas')


class Professor(Curso):
    def __init__(self, nome_curso, materias, quant_aulas, quant_alunos):
        super().__init__(nome_curso, materias, quant_aulas, quant_alunos)
        self._salario = 0


    def get_salario(self):
        return self._salario


    def set_salario(self, valor):
        if valor >= 0:
            self._salario = valor
        else:
            print('Erro: Salário inválido.')

    def apresentar(self):
        print("+", "-" * 30, "+")
        print(f"Olá, sou o(a) Professor(a) do curso: {self.get_nome_curso()}\n"
              f"Minha matéria é: {self.get_materias()},\n"
              f"Aplico {self.get_quant_aulas()} aulas por mês,\n"
              f"E tenho {self.get_quant_alunos()} alunos.")
        print("-" * 20)

        if self.get_quant_aulas() == 0:
            print('Você não aplica nenhuma aula.')
        elif 0 < self.get_quant_aulas() <= 5:
            print('Você está começando, poucas aulas, mas está indo bem!')
        elif 5 < self.get_quant_aulas() <= 10:
            print('Você está começando bem, um salário básico.')
        elif 10 < self.get_quant_aulas() <= 25:
            print('Um salário de nível médio, referente a um tempo mediano de carreira.')
        elif 25 < self.get_quant_aulas() <= 50:
            print('Um bom salário, já atingiu um nível adequado.')
        elif 50 < self.get_quant_aulas() <= 70:
            print('Um salário muito bom, referente a um tempo mais longo de carreira.')
        else:
            print('Um ótimo salário, muita experiência.')

    def salario(self):
        self._salario = self.get_quant_aulas() * 50
        print(f"De acordo com suas aulas, seu salário é R$ {self.get_salario():.2f}")


p1 = Curso('Vinícius', 'Matemática', 6, 55)
p1.apresentar()
p1.matriculas()
print('-------------------------------')


p2 = Curso('Dener', 'Português', 15, 20)
p2.apresentar()
p2.matriculas()
print('-------------------------------')


p3 = Curso('Guilherme', 'Geografia', 5, 30)
p3.apresentar()
p3.matriculas()
print('-------------------------------')

prof1 = Professor('Dener', 'Português', 40, 20)
prof1.apresentar()
prof1.salario()
print('-------------------------------')

prof2 = Professor('Lê Maia', 'História', 0, 0)
prof2.apresentar()
prof2.salario()
print('-------------------------------')

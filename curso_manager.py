class Curso:
    def __init__(self, nome_curso, materias, quant_aulas, quant_alunos, mensalidades=0):

        self.nome_curso = nome_curso
        self.materias = materias

        # Converter `quant_aulas` e `quant_alunos` para inteiros
        self.quant_aulas = int(quant_aulas)
        self.quant_alunos = int(quant_alunos)
        self.mensalidades = mensalidades

    def apresentar(self):
        print(f'Olá sou o aluno(a) {self.nome_curso} desse curso,\n'
              f'minha matéria favorita é {self.materias},\n'
              f'e tenho {self.quant_aulas} aulas semanais \n'
              f'e meu curso tem {self.quant_alunos} alunos.\n'
              f'Situação atual:')
        print('-' * 20)

        if self.quant_alunos == 0:
            print(f'O curso não teve nenhuma matrícula realizada no mês.')
        elif self.quant_alunos <= 10:
            print(f'O curso está começando a receber mensalidades. Atualmente, temos {self.quant_alunos} estudantes.')
        elif 10 < self.quant_alunos <= 50:
            print(f'O curso está bastante popular! Atualmente, temos {self.quant_alunos} mensalidades.')
        else:
            print(f'O curso está muito popular! Número de mensalidades: {self.quant_alunos}')

    def matriculas(self):
        if self.quant_alunos == 0:
            print('Nenhuma matrícula foi realizada ainda.')
        elif self.quant_alunos <= 10:
            print('Poucos alunos, mas é um bom começo.')
        elif 10 < self.quant_alunos <= 50:
            print('Bastantes alunos no curso, muito bom!')
        else:
            print(f'O curso possui atualmente {self.quant_alunos} matrículas.')


class Professor(Curso):
    def __init__(self, nome_curso, materias,
                 quant_aulas, quant_alunos, salario=0, mensalidades=0):
        super().__init__(nome_curso,materias,quant_aulas, quant_alunos, salario)
        self.mensalidades = mensalidades
        self.quant_aulas = int(quant_aulas)
        self.quant_alunos = int(quant_alunos)

        self.salario = 0

    def apresentar(self):
        print(f'Professor: Dener\n'
              f'Minha materia é {self.materias}\n'
              f'Aplico: {self.quant_aulas} aulas por mês\n'
              f'e tenho {self.quant_alunos} alunos.')
        print('-' * 20)

        if self.quant_aulas == 0:
            print(f'você aplica nenhuma aula')

        elif 0 > self.quant_aulas <= 10:
            print(f' Você está começando bem, um salário básico')

        elif 10 >= self.quant_aulas <= 25:
            print(f'um salário de nível médio, referente um tempo mediano de carreira')

        elif 25>= self.quant_aulas < 50:
            print(f'um bom salário, já atingiu um nível adequado')

        elif 50 >= self.quant_aulas <= 70:
            print(f'um salário muito bom, referente um tempo mais longo de carreira')

        else:
            print(f'um ótimo salário, muita experiência')


    def trabalhar(self):
        if self.quant_aulas == 0:
            self.salario = 0
            print(f'De acordo com suas aulas, seu salário será de R${self.salario}')

        elif 0> self.quant_aulas <= 15:
            self.salario = 1500
            print(f'De acordo com suas aulas,seu salário sera de R${self.salario}')

        elif 15 >= self.quant_aulas <= 30:
            self.salario = 4000
            print(f'De acordo com suas aulas,seu salário sera de R${self.salario}')

        elif 30 >= self.quant_aulas <=50:
            self.salario = 5500
            print(f'De acordo com suas aulas,seu salário sera de R${self.salario}')

        elif 50 >= self.quant_aulas <=70:
            self.salario = 6500
            print(f'De acordo com suas aulas, seu salário está ótimo {self.salario}')

        else:
            self.salario = 10000
            print(f'De acordo com suas aulas,MUITO BOM,o seu salário sera de R${self.salario}')


p1 = Curso('Vinícius', 'Matemática', 7, 5)
# p1.apresentar()
# p1.matriculas()

p2 = Curso('Dener', "Portugues", 5, 20)
# p2.apresentar()
# p2.matriculas()

p3 = Professor('Dener', 'Portugues', 11, 40)
p3.apresentar()
p3.trabalhar()


p4 = Professor('Lê maia', 'História', 10, 20)
# p4.apresentar()
# p4.trabalhar()




class Curso:
    def __init__(self, nome_curso, materias, quant_aulas, quant_alunos, mensalidades=0):
        self.nome_curso = nome_curso
        self.materias = materias
        self.quant_aulas = int(quant_aulas)
        self.quant_alunos = int(quant_alunos)
        self.mensalidades = mensalidades

    def apresentar(self):
        print(f'Olá, sou aluno(a) do curso do professor(a) {self.nome_curso},\n'
              f'Minha matéria favorita é {self.materias},\n'
              f'Tenho {self.quant_aulas} aulas semanais\n'
              f'E meu curso tem {self.quant_alunos} alunos.\n'
              f'Situação atual:')
        print('-' * 20)

        if self.quant_alunos == 0:
            print(f'O curso não teve nenhuma matrícula realizada no mês.')
        elif self.quant_alunos <= 10:
            print(f'O curso está começando a receber mensalidades. Atualmente, temos {self.quant_alunos} mensalidades.')
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
    def __init__(self, nome_curso, materias, quant_aulas, quant_alunos, mensalidades=0):
        super().__init__(nome_curso, materias, quant_aulas, quant_alunos, mensalidades)
        self.salario = 0

    def apresentar(self):
        print(f'Olá, sou o(a) Professor(a) de {self.nome_curso}\n'
              f'Minha matéria é {self.materias}\n'
              f'Aplico {self.quant_aulas} aulas por mês\n'
              f'E tenho {self.quant_alunos} alunos.')
        print('-' * 20)

        if self.quant_aulas == 0:
            print('Você não aplica nenhuma aula.')

        elif 0 < self.quant_aulas <= 5:
            print('Você está começando, poucas aulas, mas referente ao seu trabalho.')
        elif 5 < self.quant_aulas <= 10:
            print('Você está começando bem, um salário básico.')
        elif 10 < self.quant_aulas <= 25:
            print('Um salário de nível médio, referente a um tempo mediano de carreira.')
        elif 25 < self.quant_aulas <= 50:
            print('Um bom salário, já atingiu um nível adequado.')
        elif 50 < self.quant_aulas <= 70:
            print('Um salário muito bom, referente a um tempo mais longo de carreira.')
        else:
            print('Um ótimo salário, muita experiência.')

    def trabalhar(self):
        self.salario = self.quant_aulas * 50  # Cada aula vale R$50
        print(f'De acordo com suas aulas, seu salário será de R${self.salario:.2f}')



p1 = Curso('Vinícius', 'Matemática', 6, 55)
p1.apresentar()
p1.matriculas()
print('-------------------------------')

p2 = Curso('Dener', "Português", 15, 20)
p2.apresentar()
p2.matriculas()
print('-------------------------------')

p3 = Professor('Dener', 'Português', 40, 40)
p3.apresentar()
p3.trabalhar()
print('-------------------------------')

p4 = Professor('Lê Maia', 'História', 4, 20)
p4.apresentar()
p4.trabalhar()
print('-------------------------------')



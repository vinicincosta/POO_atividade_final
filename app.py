from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)
app.config['SECRET_KEY'] = "SECRET"

class Curso:
    def __init__(self, materias, quant_aulas, nome_alunos):

        self.nome_alunos = nome_alunos
        self.materias = materias
        self.quant_aulas = quant_aulas




    def apresentar(self):
        print(f'Olá sou o aluno(a) {self.nome_alunos} desse curso,\n'
              f'minha matéria favorita é {self.materias},\n'
              f'e tenho aulas {self.quant_aulas}')
        print('-' * 20)





p1 = Curso ('matematica', 'onlines', 'vini')
p1.apresentar()



class Professor(Curso):
    def __init__(self, nome, escola, data_nascimento, salario = 0, quant_aulas= 0):
        super().__init__(materias, quant_aulas= 0, nome_alunos, salario = 0)
        self.salario = 0
        self.quant_aulas=0


    def apresentar(self):
        print(f'Professo: Dener\n'
              f'Matéria: Matemática\n'
              f'Data Nascimento: 20/12/200')



    def trabalhar(self):

from dataclasses import dataclass

@dataclass
class Student:
    name: str
    classes: str
    grade_list: list


    def add_grade(self, unit):

        for _ in range(unit):
            
            type = input("Digite o tipo da nota: ")
            value = float(input(f"Digite sua nota da Unidade {_ + 1}: "))
            while value > 10 or value < 0:
                value = float(input(f"Digite sua nota da Unidade {_ + 1 }: "))

            grade = {'type': type, 'value': value}
            self.grade_list.append(grade)

    def calcule_avarage(self):

        soma = 0

        for grade in self.grade_list:
            soma += grade['value']

        avarage = soma / len(self.grade_list)

        return avarage
    
    def generate_report(self):
        
        print(f"""{'=' * 30}
{'RELATORIO DE DESEMPENHO'.center(30)}
{'=' * 30}

Aluno: {self.name}
Turma: {self.classes}

Notas:
- Provas: [{', '.join(str(grade['value']) for grade in self.grade_list if grade['type'] == 'Prova' )}]
- Trabalhos: [{', '.join(str(grade['value']) for grade in self.grade_list if grade['type'] == 'Trabalho')}]
- Atividades Extras: [{', '.join(str(grade['value']) for grade in self.grade_list if grade['type'] == 'Extra')}]

Média Geral: {self.calcule_avarage():.2f}
Desempenho: Bom desempenho

{'=' * 30}""")



student = Student(name="Mano", classes="Turma 01", grade_list=[])

student.add_grade(3)
print(student.calcule_avarage())
student.generate_report()
from dataclasses import dataclass
from student import Student
from classe import Classes

@dataclass
class Report:
    student: Student
    classes: Classes


    def generate_report(self):

        relatorio = f"""{'=' * 30}
{'RELATORIO DE DESEMPENHO'.center(30)}
{'=' * 30}

Aluno: {self.student.name}
Turma: {self.classes.name_class if self.student in self.classes.students_list else "Nenhuma"}

"""

        types_grade = {}
        soma = 0
        for grade in self.student.grade_list:
            if grade['type'] not in types_grade:
                types_grade[grade['type']] = []
            types_grade[grade['type']].append(grade['value'])

        for type, value in types_grade.items():
            soma = 0
            for v in value:
                soma += v
            media = soma / len(value)
            print(value)
            relatorio += f"- {type.upper()} Notas {value} :media = {media}\n"

        total_media = self.student.calcule_avarage()

        # Classificação do desempenho
        if total_media >= 9:
            desempenho = "Excelente desempenho!"
        elif total_media >= 7:
            desempenho = "Bom desempenho! Continue assim."
        elif total_media >= 5:
            desempenho = "Desempenho regular, precisa melhorar."
        else:
            desempenho = "Desempenho insuficiente. Requer atenção."

        relatorio += f"\nDesempenho: {desempenho}\n"
        relatorio += '=' * 30

        return relatorio
    
aluno = Student(name="Mano", grade_list=[])
turma = Classes(name_class="Turma 01", students_list=[aluno])
relatorio = Report(student=aluno, classes=turma)
aluno.add_grade(4)
print(aluno)
relatorio.generate_report()
print(relatorio.generate_report())

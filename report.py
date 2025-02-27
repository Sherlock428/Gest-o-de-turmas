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
        
        for grade in self.student.grade_list:
            if grade['type'] not in types_grade:
                types_grade[grade['type']] = []
            types_grade[grade['type']].append(grade['value'])

        for type, value in types_grade.items():
            soma = 0
            for v in value:
                soma += v
            media = soma / len(value)
            
            notas_f = ", ".join(str(v) for v in value) 
            relatorio += f"- {type.capitalize()} {notas_f } | Media = {media}\n"

        total_media = self.student.calcule_avarage()
        
        relatorio += f"\nMedia Final: {total_media:.2f}"
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
    
# aluno = Student(id=1, name="Mano", grade_list=[])
# turma = Classes(name_class="Turma 01", students_list=[aluno])
# turma01 = Classes(name_class="Turma 02", students_list=[aluno])
# relatorio = Report(student=aluno, classes=turma)
# aluno.add_grade()
# aluno.add_grade()
# aluno.add_grade()
# print(aluno)
# relatorio.generate_report()
# print(relatorio.generate_report())

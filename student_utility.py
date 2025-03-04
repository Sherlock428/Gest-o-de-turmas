from report import Report
from classe import Classes
from student import Student
from datetime import datetime

def main_student(student, classe):

    while True:
        print(f"""
{'=' * 30}
{student.name.center(30)}
{'=' * 30}

[1] Ver notas e Médias
[2] Ver Atividades e Lembretes
[3] Relatorio de Desempenho
[4] Sair""")
        
        try:
            option = int(input("Escolha: "))

            if option == 1:
                student.display_grade()
            elif option == 2:
                student.lembrete_task()
            elif option == 3:
                report = Report(student=student, classes=classe)
                print(report.generate_report())

            else:
                return
        except (ValueError, TypeError) as e:
            print(f"ERROR: Digite um valor válido {e}")

classe = Classes(name_class="Turma 01", code_class=1111, students_list=[Student(id=1, name="Mano", task=[{"description": "Ativadade página 1", "date_delivery": datetime.strptime("04/03/2025", "%d/%m/%Y"), "type": "task","status": "Pendente"}, {"description": "Ativadade página 2", "date_delivery": datetime.strptime("02/03/2025", "%d/%m/%Y"), "type": "task","status": "Pendente"}, {"description": "Ativadade página 3", "date_delivery": datetime.strptime("04/03/2025", "%d/%m/%Y"), "type": "extra","status": "Pendente"}], code=123, grade_list=[{"type": "Provas", "value": 10}, {"type": "Provas", "value": 10}, {"type": "Provas", "value": 10}, {"type": "Trabalhos", "value": 10}])])
aluno = classe.students_list[0]
main_student(aluno, classe)



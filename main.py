from student import Student
from classe import Classes
from report import Report




def report(classe):

    classe.all_students()

    n = int(input("\nEscolha: "))

    if 1 <= n <= len(classe.students_list):
        student_select = classe.students_list[n - 1]

        new_report = Report(student=student_select, classes=classe)
        print(new_report.generate_report())
        

def ativity():
    pass

def main():

    classe = Classes(name_class="Turma 01", students_list=[Student(id=1, name="Mano", grade_list=[{"type": "Provas", "value": 10}, {"type": "Provas", "value": 9}, {"type": "Provas", "value": 8}, {"type": "Trabalhos", "value": 9}])])
    while True:
        print(f"""
{'=' * 30}
{classe.name_class.center(30)}
{'=' * 30}

[1] Adicionar Aluno
[2] Remover Aluno
[3] Ver Todos Alunos
[4] Exibir Relatorio
""")
        
        try:
            option = int(input("Escolha: "))

            if option == 1:
                classe.add_student()
            elif option == 2:
                classe.remove_student()
            elif option == 3:
                classe.all_students()
            elif option == 4:
                report(classe)
            elif option == 5:
                ativity()
            else:
                return
        except (ValueError, TypeError) as e:
            print(f"ERROR: Digite um valor válido {e}")

main()
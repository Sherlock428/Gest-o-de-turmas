from student import Student
from classe import Classes
from report import Report


def report(classe, student):

    classe.all_student()

    n = int(input("Escolha: "))

    if 1 <= n <= len(student.grade_list):
        student_select = student.grade_list[n - 1]

        new = Report(student=student_select, classes=classe)
def main():

    classe = Classes(name_class="Turma 01", students_list=[])
    while True:
        print(f"""
TURMA

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
                pass
            else:
                return
        except (ValueError, TypeError):
            print("ERROR: Digite um valor válido")

main()
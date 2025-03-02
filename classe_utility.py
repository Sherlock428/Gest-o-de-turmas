from student import Student
from classe import Classes
from report import Report
from datetime import datetime

def report(classe):

    classe.all_students()

    n = int(input("\nEscolha: "))

    if 1 <= n <= len(classe.students_list):
        student_select = classe.students_list[n - 1]

        new_report = Report(student=student_select, classes=classe)
        print(new_report.generate_report())
        

def activity(classe):
    
    print(f"""
[1] Atividade Lembrete
[2] Passar atividade Manualmente
[3] Sair
""")
    
    option = int(input("Escolha: "))

    
    if option == 1:
        description = input("Digite a descrição do lembrete: ")
        while True:
            try:
                date = input("Digite o prazo em dd/mm/yy")
                date_delivery = datetime.strptime(date, "%d/%m/%Y")
                if date_delivery >= datetime.now():
                    break
                else:
                    print("Error:  um prazo deve ser uma data futuro")
                    print("Se desejar cancelar operação digite 0")

                    e = int(input("Digite '0' para cancelar o lembrete: "))

                    if e == "0":
                        return
            
            except (ValueError, TypeError):
                print("ERROR Digite um valor válido")

    
        ativity = {
            "description": description,
            "date_delivry": date_delivery,
            "status": "Pendente"
        }

        for student in classe.students_list:
            ativity.append(student.task)
    
    elif option == 2:
        pass
    elif option == 3:
        print("Retornando")
        
def main(student):

    classe = Classes(name_class="Turma 01", code_class=1111, students_list=[Student(id=1, name="Mano", code=123, task=[], grade_list=[{"type": "Provas", "value": 10}, {"type": "Provas", "value": 10}, {"type": "Provas", "value": 9}, {"type": "Trabalhos", "value": 9}])])
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
                activity(student)
            else:
                return
        except (ValueError, TypeError) as e:
            print(f"ERROR: Digite um valor válido {e}")

main()
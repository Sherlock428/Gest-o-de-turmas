from report import Report

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
                student.see_grade()
            elif option == 2:
                pass
            elif option == 3:
                report = Report(student=student, classes=classe)
                print(report.generate_report())

            else:
                return
        except (ValueError, TypeError) as e:
            print(f"ERROR: Digite um valor válido {e}")



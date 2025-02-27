
def login_student(classe):

    try:
        name = input("Digite o username: ")
        code = input("Digite o code de 3 dígitos: ")
        while len(code) != 3 or not code.isdigit():
            print("Error: código deve conter 3 dígitos e apenas números")
            code = input("Digite o code de 3 dígitos")            

        for student in classe.students_list:
            if name == student.name and code == student.code:
                print(f"Aluno encontrado com sucesso {student.name}")
                
                return student
            
        print("Usuario não encontrado")
        input('')
    except (ValueError, TypeError):
        print("ERROR: Digite um valor válido")

def classe_login(classe):
    try:
        classname = input("Digite o nome da classe")
        code = input("digite o código de 4 dígitos")
        while len(code) != 4 or not code.isdigit():
            print("Error: código deve conter 4 dígitos e apenas números")
            code = input("Digiite o código de 4 dígiitos")

        if classname == classe.name_class and code == classe.code:
            return classe
        
        print("Turma não encontrada")
        input()
    except (ValueError, TypeError):
        print("ERROR: Digite um valor válido")


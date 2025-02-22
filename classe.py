from dataclasses import dataclass
from student import Student

@dataclass
class Classes: 
    name_class: str
    students_list: list

    def all_students(self):
        for i, student in enumerate(self.students_list, start=1):
            notas = ", ".join(f"- {nota['type']}: {nota['value'] }" for nota in student.grade_list)
            print(f"""
ID: [{student.id}]
Nome: {student.name}

========Notas========

{notas if notas else "Nehum nota encontrada"}""")
    def add_student(self):
        name = input("Digite o nome do Aluno: ")
        id = len(self.students_list) + 1
        new_student = Student(id=id, name=name, grade_list=[])

        self.students_list.append(new_student)

        print("Bem_vindo a turma")

        return new_student

    def remove_student(self):
        
        # for i, student in enumerate(self.students_list, start=1):
        #     print(f"[{i}] {student.name}")

        n = int(input("Escolha o aluno que deseja deletar: "))

        if 1 <= n <= len(self.students_list):
            deleted_student = self.students_list[n - 1]
            self.students_list.pop(n - 1)

            print(f"O estudante {deleted_student.name} foi removido da turma")

classe = Classes(name_class="TURMA 01", students_list=[])


from student_utility import main_student
from classe import Classes
from student import Student

classe = Classes(name_class="Turma 01", code_class=1111, students_list=[Student(id=1, name="Mano", task=[], code=123, grade_list=[{"type": "Provas", "value": 10}, {"type": "Provas", "value": 10}, {"type": "Provas", "value": 10}, {"type": "Trabalhos", "value": 10}])])
aluno = classe.students_list[0]

main_student(aluno, classe)
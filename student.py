from dataclasses import dataclass

@dataclass
class Student:
    name: str
    grade_list: list


    def add_grade(self, unit):

        for _ in range(unit):
            grade = float(input(f"Digite sua nota da Unidade {_ + 1}: "))
            self.grade_list.append(grade)

    def calcule_avarage(self):

        soma = 0

        for grade in self.grade_list:
            soma += grade

        avarage = soma / len(self.grade_list)

        return avarage
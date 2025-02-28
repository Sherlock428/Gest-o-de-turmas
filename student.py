from dataclasses import dataclass


@dataclass
class Student:
    id: int
    name: str
    code: int
    task: list
    grade_list: list


    def add_grade(self):

        type = input("Digite o tipo da nota: ")
        unit = int(input(f"Qual a quantidade de unidades para notas em {type}: "))
        for _ in range(unit):
            
            value = float(input(f"Digite sua nota da Unidade {_ + 1}: "))
            while value > 10 or value < 0:
                value = float(input(f"Digite sua nota da Unidade {_ + 1 }: "))

            grade = {'type': type, 'value': value}
            self.grade_list.append(grade)

    def calcule_avarage(self):

        soma = 0

        for grade in self.grade_list:
            soma += grade['value']

        avarage = soma / len(self.grade_list)

        return avarage
    
    def display_grade(self):
        
        grouped_grade = {}
        for grade in self.grade_list: 

            if grade['type'] not in grouped_grade:
                grouped_grade[grade['type']] = []
            grouped_grade[grade['type']].append(grade['value'])
        
        for type, value in grouped_grade.items():
            sum = 0
            for v in value:
                sum += v
            media = sum / len(value)
        grades = "\n".join(f"{type}: {', '.join(map(str, grade))}: Média: {media}" for type, grade in grouped_grade.items())

        print(f"""
{'=' * 30}
{'Notas e Médias'.center(30)}
{'=' * 30}

{grades}

Média Final: {self.calcule_avarage():.2f}
""")
        


#     def generate_report(self):
        
#         print(f"""{'=' * 30}
# {'RELATORIO DE DESEMPENHO'.center(30)}
# {'=' * 30}

# Aluno: {self.name}
# Turma: {self.classes}

# Notas:
# - Provas: [{', '.join(str(grade['value']) for grade in self.grade_list if grade['type'] == 'Prova' )}]
# - Trabalhos: [{', '.join(str(grade['value']) for grade in self.grade_list if grade['type'] == 'Trabalho')}]
# - Atividades Extras: [{', '.join(str(grade['value']) for grade in self.grade_list if grade['type'] == 'Extra')}]

# Média Geral: {self.calcule_avarage():.2f}
# Desempenho: Bom desempenho

# {'=' * 30}""")






ids = [1, 2, 3]
names = ['Alice', 'Bob', 'Cathy', 'Mike']
grades = ['A', 'B', 'A+', 'A']

students = list(zip(ids, zip(names, grades)))
print(students)

students_dict = {id: {'name': name, 'grade': grade} for id, (name, grade) in students}
print(students_dict)

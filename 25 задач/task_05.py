import json
students = 'students.json'
max_score = 0
max_student = ''
with open(students, 'r') as file:
    students_data = json.load(file)
    for l in students_data:
        l['passed'] = l['score'] >= 60
        if l['score'] > max_score:
            max_score = l['score']
            max_student = l['name']
    print(max_student)
    with open('new_students.json', 'w') as file:
        json.dump(students_data, file, indent=4, ensure_ascii=False)
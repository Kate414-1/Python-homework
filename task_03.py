import csv
students_count = 0
students_sum = 0
max_score = 0
best_student = None
group_score = {}
with open('students.csv') as f:
    reader = csv.reader(f, delimiter=',')
    headers = next(reader)
    for row in reader:
        students_count += 1
        students_sum += int(row[2])
        if int(row[2]) > max_score:
            max_score = int(row[2])
            best_student = row[0]
        if row[1] not in group_score:
            group_score[row[1]] = [1, int(row[2])]
        else:
            previous_count, previous_sum = group_score[row[1]]
            group_score[row[1]] = [previous_count + 1, previous_sum + int(row[2])]
print(students_sum / students_count)
print(best_student)
for group_number, group_data in group_score.items():
    print(group_number, group_data[1] / group_data[0])
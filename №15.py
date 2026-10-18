def count_lines(stream):
    count = 0
    for line in stream:
        count += 1
    return count

#Тесты
from io import StringIO
data = StringIO('first\nsecond\nthird')
print(count_lines(data))

with open('data.txt','r',encoding='utf-8') as f:
    print(count_lines(f))
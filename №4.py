import csv
from csv import DictReader
with open('fail_csv.csv') as f:
    with open('expensive.csv','w',encoding='utf-8',newline='') as d:
        reader = DictReader(f)
        writer = csv.DictWriter(d, fieldnames=reader.fieldnames)
        writer.writeheader()
        for row in reader:
            if int(row['price']) > 100:
                writer.writerow(row)
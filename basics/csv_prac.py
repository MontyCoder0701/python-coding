import csv

data = [
    ["이름", "반", "번호"],
    ["재석", 1, 20],
    ["홍철", 3, 8],
    ["형돈", 10, 3],
]

file = open("student.csv", "w", newline="", encoding="utf-8-sig")
writer = csv.writer(file)

for d in data:
    writer.writerow(d)

file.close()

file = open("student.csv", "r", encoding="utf-8-sig")
reader = csv.reader(file)

for d in reader:
    print(d)
file.close()

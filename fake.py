from faker import Faker
import random
import csv

# create fake data for 100 students
fake = Faker()
students = []
for i in range(20):
    name = fake.name()
    english = random.randint(50, 100)
    hindi = random.randint(50, 100)
    maths = random.randint(50, 100)
    students.append([name, english, hindi, maths])

# write the data to a CSV file
with open("student_marks.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["Name", "English", "Hindi", "Maths"])
    writer.writerows(students)



# GENERATE FAKE DATAS 

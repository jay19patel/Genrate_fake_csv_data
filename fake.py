from faker import Faker
import random
import csv

# create fake data for 100 students
fake = Faker()
students = []
for i in range(100):
    name = fake.name()
    email = fake.email()
    hindi = random.randint(50, 100)
    maths = random.randint(50, 100)
    students.append([name,email, hindi, maths])

# write the data to a CSV file
with open("student_marks.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["Name", "Email", "Hindi", "Maths"])
    writer.writerows(students)



# GENERATE FAKE DATAS 
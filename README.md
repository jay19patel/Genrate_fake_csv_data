# Genrate_fake_csv_data

# import moduls
- import faker modul :
 ```python
    from faker import Faker
    import csv
    import random
```
# create fake data for 100 students
```python
fake = Faker()
students = [] #list for saving data 
for i in range(100):
    name = fake.name()
    english = random.randint(50, 100)
    hindi = random.randint(50, 100)
    maths = random.randint(50, 100)
    students.append([name, english, hindi, maths])
```
# write the data to a CSV file
```python 
with open("student_marks.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["Name", "English", "Hindi", "Maths"])
    writer.writerows(students)
```





## Person
    name
    first_name
    last_name
    prefix
    suffix
    job
    email
    phone_number
    company
    address
    country
    city
    postcode
    latitude
    longitude
    ssn
    profile

## Date and Time
    date
    time
    date_time
    iso8601
    day_of_week
    month_name
    year
    timezone

## Text
    text
    sentence
    sentences
    paragraph
    paragraphs
    word
    words
    sentence
    sentences
    text
    text

## Internet
    ipv4
    ipv6
    url
    uri
    domain_name
    user_name
    password

## Finance
    credit_card_number
    credit_card_provider
    credit_card_security_code

## Miscellaneous
    color_name
    file_name
    language_code
    mime_type
    phone_number
    ssn
    uuid4
    hex_color
    currency_code
    credit_card_expire

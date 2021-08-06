import csv
import os
import random
from datetime import datetime
from decimal import Decimal
import random
from faker import Faker


fake = Faker()


def create_csv_file_Instructors_Info():
    time_stampe = datetime.now().strftime("%Y_%m_%d-%I_%M_%S_%p")
    raw_path = os.path.dirname(__file__)
    with open(f'{raw_path}\InstructorData-{time_stampe}.csv', 'w', newline='') as csvfile:
        fieldnames = ['Instructor_ID','Instructor_Name', 'Instructor_email','Instructor_address','Instructor_PhoneNum', 'Instructor_level', 'Total_courses_released', 'Instructor_ranked' ]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        RECORD_COUNT = 100
        writer.writeheader()
        for i in range(RECORD_COUNT):
            writer.writerow(
                {
                    'Instructor_ID': i,
                    'Instructor_Name': fake.name(),
                    'Instructor_email': fake.email(),
                    'Instructor_address': fake.address(),
                    'Instructor_PhoneNum': fake.msisdn(),
                    'Instructor_level': random.choice(['None', 'Bacherlor', 'Master', 'Doctor', 'Professor', 'Other']),
                    'Total_courses_released': fake.random_int(1,100),
                    'Instructor_ranked': fake.random_int(1,5)
                }
            )
            
def create_csv_file_Courses_Info():
    # pdb.set_trace()
    time_stampe = datetime.now().strftime("%Y_%m_%d-%I_%M_%S_%p")
    raw_path = os.path.dirname(__file__)
    with open(f'{raw_path}\CoursesData-{time_stampe}.csv', 'w', newline='') as csvfile:
        fieldnames = ['Course_ID','Course_Name','Instructor_ID','Total_hours', 'Price' ]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        RECORD_COUNT = 1000
        writer.writeheader()
        for i in range(RECORD_COUNT):
            writer.writerow(
                {
                    'Course_ID': i,
                    'Course_Name': fake.name(),
                    'Instructor_ID': fake.random_int(1,20),
                    'Total_hours': fake.random_int(1,100),
                    'Price': fake.pricetag()
                }
            )

if __name__ == '__main__':
    print('Creating a fake data...')
    create_csv_file_Instructors_Info()
    create_csv_file_Courses_Info()


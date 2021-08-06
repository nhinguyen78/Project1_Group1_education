import csv
import os
import random
from datetime import datetime
import time
from decimal import Decimal
import random
from faker import Faker


fake = Faker()


def create_csv_file_Instructors_Info():
    time_stampe = datetime.now().strftime("%Y_%m_%d-%I_%M_%S_%p")
    raw_path = os.path.dirname(__file__)
    with open(f'{raw_path}\InstructorData-{time_stampe}.csv', 'w', newline='') as csvfile:
        fieldnames = ['Instructor_ID','Instructor_Name', 'Instructor_email','Instructor_address','Instructor_PhoneNum', 'Instructor_level', 'Total_courses_released', 'Instructor_ranked','Gender']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        RECORD_COUNT = 100
        writer.writeheader()
        for i in range(RECORD_COUNT):
            writer.writerow(
                {
                    'Instructor_ID': i,
                    'Instructor_Name': fake.name(),
                    'Gender':random.choice(['Male', 'Female']),
                    'Instructor_email': fake.email(),
                    'Instructor_address': fake.address(),
                    'Instructor_PhoneNum': fake.msisdn(),
                    'Instructor_level': random.choice(['None', 'Bacherlor', 'Master', 'Doctor', 'Professor', 'Other']),
                    'Total_courses_released': fake.random_int(1,20),
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

def str_time_prop(start, end, time_format, prop):
    """Get a time at a proportion of a range of two formatted times.
    start and end should be strings specifying times formatted in the
    given format (strftime-style), giving an interval [start, end].
    prop specifies how a proportion of the interval to be taken after
    start.  The returned time will be in the specified format.
    """

    stime = time.mktime(time.strptime(start, time_format))
    etime = time.mktime(time.strptime(end, time_format))

    ptime = stime + prop * (etime - stime)

    return time.strftime(time_format, time.localtime(ptime))

def random_date(start, end, prop):
    return str_time_prop(start, end, '%m/%d/%Y', prop)


def create_csv_file_Transactions():
    time_stampe = datetime.now().strftime("%Y_%m_%d-%I_%M_%S_%p")
    raw_path = os.path.dirname(__file__)
    with open(f'{raw_path}\TracsactionData-{time_stampe}.csv', 'w', newline='') as csvfile:
        fieldnames = ['Index','Transaction_ID','Instructor_ID', 'Course_ID', 'Student_ID','Instructor_ranked','Date']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        RECORD_COUNT = 1000
        writer.writeheader()
        for i in range(RECORD_COUNT):
            writer.writerow(
                {
                    'Index': i,
                    'Transaction_ID': fake.random_int(1,1000),
                    'Instructor_ID': fake.random_int(1,10),
                    'Course_ID': fake.random_int(1,20),
                    'Student_ID':fake.random_int(1,1000),
                    'Instructor_ranked': fake.random_int(1,5),
                    'Date': random_date("1/1/2017", "6/1/2021", random.random())
                }
            ) 
            
def create_csv_file_Students_Info():
    time_stampe = datetime.now().strftime("%Y_%m_%d-%I_%M_%S_%p")
    raw_path = os.path.dirname(__file__)
    with open(f'{raw_path}\StudentData-{time_stampe}.csv', 'w', newline='') as csvfile:
        fieldnames = ['Index','Student_ID', 'Name','Gender','Email','Address','PhoneNumber', 'Final_Score', 'Rating_class', 'Rating_teacher','Class_recommendation' ]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        RECORD_COUNT = 1000
        writer.writeheader()
        for i in range(RECORD_COUNT):
            writer.writerow(
                {
                    'Index': i,
                    'Student_ID':fake.random_int(1,1000),
                    'Name': fake.name(),
                    'Gender': random.choice(['Male', 'Female']),
                    'Email': fake.email(),
                    'Address': fake.address(),
                    'PhoneNumber': fake.msisdn(),
                    'Final_Score': fake.random_int(1,10),
                    'Rating_class': fake.random_int(1,5),
                    'Rating_teacher':fake.random_int(1,5),
                    'Class_recommendation':bool(random.getrandbits(1))
                }
            )
            
if __name__ == '__main__':
    print('Creating a fake data...')
    create_csv_file_Instructors_Info()
    create_csv_file_Students_Info()
    create_csv_file_Courses_Info()
    create_csv_file_Transactions()



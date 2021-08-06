import csv
import os
import random
from datetime import datetime
from decimal import Decimal
from faker import Faker


fake = Faker()

reviews_words_list=[
]


def create_csv_file_Fact_table():
    time_stampe = datetime.now().strftime("%Y_%m_%d-%I_%M_%S_%p")
    raw_path = os.path.dirname(__file__)
    with open(f'{raw_path}\FACT_table-{time_stampe}.csv', 'w', newline='') as csvfile:
        fieldnames = ['Line_Item_ID','Class_ID', 'Teacher_ID','Course_ID','Quantity', 'Ratings','Reviews']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        RECORD_COUNT = 100
        writer.writeheader()
        for i in range(RECORD_COUNT):
            writer.writerow(
                {
                    'Line_Item_ID': i,
                    'Class_ID': fake.random_int(0,30),
                    'Teacher_ID': fake.random_int(1,15),
                    'Course_ID': fake.random_int(1,20),
                    'Quantity': fake.random_int(25,30),
                    'Ratings': fake.random_int(1,5),
                    'Reviews': fake.text()
                }
            )

if __name__ == '__main__':
    print('Creating a fake data...')
    create_csv_file_Fact_table()
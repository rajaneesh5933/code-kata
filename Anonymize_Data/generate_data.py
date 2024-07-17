import csv
import argparse
from faker import Faker

fake = Faker()


def generate_random_data(num_records, filename):
    with open(filename, 'w', newline='') as csvfile:
        fieldnames = ['first_name', 'last_name', 'address', 'date_of_birth']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()
        for _ in range(num_records):
            writer.writerow({
                'first_name': fake.first_name(),
                'last_name': fake.last_name(),
                'address': fake.address(),
                'date_of_birth': fake.date_of_birth()
            })


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Generate a CSV file with random data.')
    parser.add_argument('--num-records', type=int, required=True, help='Number of records to generate.')
    parser.add_argument('--output', type=str, required=True, help='Output CSV file name.')

    args = parser.parse_args()

    generate_random_data(args.num_records, args.output)

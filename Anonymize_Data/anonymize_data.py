import csv
import hashlib
import argparse


def anonymize_value(value):
    return hashlib.sha256(value.encode()).hexdigest()


def anonymize_csv(input_filename, output_filename):
    with open(input_filename, 'r') as csvfile, open(output_filename, 'w', newline='') as outputfile:
        reader = csv.DictReader(csvfile)
        fieldnames = reader.fieldnames
        writer = csv.DictWriter(outputfile, fieldnames=fieldnames)

        writer.writeheader()
        for row in reader:
            row['first_name'] = anonymize_value(row['first_name'])
            row['last_name'] = anonymize_value(row['last_name'])
            row['address'] = anonymize_value(row['address'])
            writer.writerow(row)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Anonymize a CSV file.')
    parser.add_argument('--input', type=str, required=True, help='Input CSV file name.')
    parser.add_argument('--output', type=str, required=True, help='Output CSV file name.')

    args = parser.parse_args()

    anonymize_csv(args.input, args.output)

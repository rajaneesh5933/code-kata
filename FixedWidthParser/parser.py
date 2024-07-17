import csv


def parse_fixed_width_to_csv(spec, input_filename, output_filename):
    with open(input_filename, 'r') as infile, open(output_filename, 'w', newline='') as outfile:
        reader = infile.readlines()
        writer = csv.writer(outfile)

        writer.writerow(spec.keys())

        for line in reader:
            row = []
            position = 0
            for field, length in spec.items():
                row.append(line[position:position + length].strip())
                position += length
            writer.writerow(row)

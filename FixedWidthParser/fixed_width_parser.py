from generator import (
    generate_random_spec,
    generate_random_data,
    generate_fixed_width_file
)
from parser import parse_fixed_width_to_csv


def main():
    spec = generate_random_spec(4)
    data = generate_random_data(spec, 10)

    generate_fixed_width_file(spec, data, 'fixed_width.txt')
    parse_fixed_width_to_csv(spec, 'fixed_width.txt', 'output.csv')

if __name__ == '__main__':
    main()
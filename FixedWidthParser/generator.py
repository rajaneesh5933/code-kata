import random

predefined_attributes = {
    'Name': 10,
    'Age': 3,
    'Country': 15,
    'Occupation': 20,
    'Department': 20,
    'Salary': 8,
    'JoiningDate': 10,
    'EmployeeID': 8
}

predefined_data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eva'],
    'Age': ['30', '25', '35', '40', '28'],
    'Country': ['USA', 'Canada', 'Australia', 'UK', 'Germany'],
    'Occupation': ['Engineer', 'Doctor', 'Artist', 'Teacher', 'Scientist'],
    'Department': ['IT', 'HR', 'Finance', 'Marketing', 'Research'],
    'Salary': ['70000', '80000', '90000', '60000', '75000'],
    'JoiningDate': ['2020-01-01', '2019-03-15', '2018-07-23', '2021-11-30', '2022-05-20'],
    'EmployeeID': ['E1234567', 'E2345678', 'E3456789', 'E4567890', 'E5678901']
}

def generate_random_spec(num_fields):
    selected_fields = random.sample(list(predefined_attributes.keys()), num_fields)
    spec = {field: predefined_attributes[field] for field in selected_fields}
    return spec

def generate_random_data(spec, num_records):
    data = []
    for _ in range(num_records):
        record = {}
        for field in spec.keys():
            record[field] = random.choice(predefined_data[field])
        data.append(record)
    return data

def generate_fixed_width_file(spec, data, filename):
    with open(filename, 'w') as file:
        for row in data:
            line = ""
            for field, length in spec.items():
                value = str(row[field])
                line += value.ljust(length)[:length]
            file.write(line + "\n")

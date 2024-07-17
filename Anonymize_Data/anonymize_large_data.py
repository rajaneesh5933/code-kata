import dask.dataframe as dd
import hashlib
import argparse


def anonymize_value(value):
    # Ensure the value is a string before anonymizing
    if not isinstance(value, str):
        value = str(value)
    return hashlib.sha256(value.encode()).hexdigest()


def anonymize_column(df, column_name):
    return df[column_name].map(anonymize_value, meta=('x', 'str'))


def anonymize_large_csv(input_filename, output_filename):
    try:
        df = dd.read_csv(input_filename,
                         dtype={'first_name': 'str', 'last_name': 'str', 'address': 'str', 'date_of_birth': 'str'},
                         assume_missing=True)

        print("Columns in the dataframe:", df.columns)

        required_columns = {'first_name', 'last_name', 'address'}
        missing_columns = required_columns - set(df.columns)
        if missing_columns:
            raise KeyError(f"Missing columns in the CSV file: {missing_columns}")

        df['first_name'] = anonymize_column(df, 'first_name')
        df['last_name'] = anonymize_column(df, 'last_name')
        df['address'] = anonymize_column(df, 'address')

        df.to_csv(output_filename, single_file=True, index=False)
    except Exception as e:
        print(f"Error processing the file: {e}")
        # Log the problematic file
        with open("error_log.txt", "w") as log_file:
            log_file.write(f"Error processing the file: {e}\n")


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Anonymize a large CSV file using Dask.')
    parser.add_argument('--input', type=str, required=True, help='Input CSV file name.')
    parser.add_argument('--output', type=str, required=True, help='Output CSV file name.')

    args = parser.parse_args()

    anonymize_large_csv(args.input, args.output)

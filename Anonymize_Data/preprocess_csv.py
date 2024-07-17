import pandas as pd
import re
from io import StringIO


def preprocess_line(line):
    return re.sub(r'(?<!^)"(?!,")(?<!,")(?!$)', '\\"', line)


def clean_csv(input_filename, output_filename, log_filename):
    chunksize = 100000
    valid_rows = 0
    header_written = False

    with open(input_filename, 'r') as infile, open(log_filename, 'w') as log_file, open(output_filename,
                                                                                        'w') as outfile:
        buffer = []
        for line in infile:
            try:
                buffer.append(preprocess_line(line))
                if len(buffer) >= chunksize:
                    data = StringIO("".join(buffer))
                    df = pd.read_csv(data, escapechar='\\', on_bad_lines='skip', engine='python')
                    if not header_written:
                        df.to_csv(outfile, mode='a', index=False, header=True)
                        header_written = True
                    else:
                        df.to_csv(outfile, mode='a', index=False, header=False)
                    valid_rows += len(df)
                    buffer = []
            except Exception as e:
                log_file.write(f"Error processing line: {line}\nException: {e}\n")

        if buffer:
            data = StringIO("".join(buffer))
            df = pd.read_csv(data, escapechar='\\', on_bad_lines='skip', engine='python')
            if not header_written:
                df.to_csv(outfile, mode='a', index=False, header=True)
                header_written = True
            else:
                df.to_csv(outfile, mode='a', index=False, header=False)
            valid_rows += len(df)

        log_file.write(f"Total valid rows written: {valid_rows}\n")

    print(f"Total valid rows written: {valid_rows}")


if __name__ == '__main__':
    import argparse

    parser = argparse.ArgumentParser(description='Clean a CSV file by removing problematic rows.')
    parser.add_argument('--input', type=str, required=True, help='Input CSV file name.')
    parser.add_argument('--output', type=str, required=True, help='Output cleaned CSV file name.')
    parser.add_argument('--log', type=str, required=True, help='Log file name for problematic rows.')

    args = parser.parse_args()

    clean_csv(args.input, args.output, args.log)

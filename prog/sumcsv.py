import argparse
import csv

def column_sum(path, column, colrange = None):
    try:
        with open(path, 'r') as file:
            reader = csv.DictReader(file)
            f = list(reader)

            if column not in reader.fieldnames:
                print(f"Column {column} not found in the file.")
                return None

            if not (colrange == None):
                start, end = map(int, colrange.split(':'))
                sum = 0
                for i in range(start, end+1):
                    sum += float(f[i][column])
                return column, sum

            else:
                c_sum = 0
                for row in f:
                    try:
                        c_sum += float(row[column])
                    except ValueError:
                        continue

                return column, c_sum
    except FileNotFoundError:
        print(f"File '{path}' not found")
        return None
    except Exception as e:
        print(e)
        return None

def main():
    parser = argparse.ArgumentParser(description='Calculate the sum of specified column in a CSV file.')
    parser.add_argument('file', help='Input path for CSV file.')
    parser.add_argument('column', nargs='*', help='Name of column to be summed.')
    parser.add_argument('--colrange', nargs='?', help='Specify range of columns to be summed.')

    args = parser.parse_args()

    try:
        for col in args.column:
            column, result = column_sum(args.file, col, args.colrange)
            if result is not None:
                print(f"Sum Of Column '{column}': {result}")
    
    except Exception as e:
        print(e)

if __name__ == "__main__":
    main()

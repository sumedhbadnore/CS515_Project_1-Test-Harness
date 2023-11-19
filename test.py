import os
import subprocess

files_directory = "test"
files = os.listdir(files_directory)

def wc_test(file_path):
    result = subprocess.check_output(['python', os.path.join('prog','wc.py'), file_path], universal_newlines=True)
    return (result)

def gron_test(file_path):
    result = subprocess.check_output(['python', os.path.join('prog','gron.py'), file_path], universal_newlines=True)
    return (result.strip())

def sumcsv_test(file_path, column):
    result = subprocess.check_output(['python', os.path.join('prog','sumcsv.py'), file_path, column], universal_newlines=True)
    return (result.strip())

def test_run():
    try:
        global files_directory
        print("------------------------ wc.py -----------------------------")
        # Run tests for wc.py
        input_files = [file for file in files if file.endswith(".in") and "wc" in file]
        output_files = [file for file in files if file.endswith(".out") and "wc" in file]

        for i in range(0, len(input_files)):
            file_path = os.path.join(files_directory, input_files[i])
            output = wc_test(file_path)
            out_file = os.path.join(files_directory, output_files[i])
            with open(out_file) as f:
                expected_output = f.read()
            try:
                assert expected_output.strip() == output.strip()
            except AssertionError:
                print(f"Failed for: {input_files[i]}")
                continue
        print("Success!")

        print("------------------------ gron.py -----------------------------")
        # Run test for gron.py
        input_files = [file for file in files if file.endswith(".in") and "gron" in file]
        output_files = [file for file in files if file.endswith(".out") and "gron" in file]

        for i in range(0, len(input_files)):
            file_path = os.path.join(files_directory, input_files[i])
            output = gron_test(file_path)
            out_file = os.path.join(files_directory, output_files[i])
            with open(out_file) as f:
                expected_output = f.read()
            try:
                assert expected_output.strip() == output.strip()
            except AssertionError:
                print(f"Failed for: {input_files[i]}")
                continue
        print("Success!")

        print("------------------------ sumcsv.py -----------------------------")
        # Run test for sumcsv.py
        input_files = [file for file in files if file.endswith(".in") and "sumcsv" in file]
        output_files = [file for file in files if file.endswith(".out") and "sumcsv" in file]

        # Column is Hardcoded work on this 
        column = "Population"

        for i in range(0, len(input_files)):
            file_path = os.path.join(files_directory, input_files[i])
            output = sumcsv_test(file_path, column)
            out_file = os.path.join(files_directory, output_files[i])
            with open(out_file) as f:
                expected_output = f.read()
            try:
                assert expected_output.strip() == output.strip()
            except AssertionError:
                print(f"Failed for: {input_files[i]}")
                continue
        print("Success!")    


if __name__ == "__main__":
    test_run()
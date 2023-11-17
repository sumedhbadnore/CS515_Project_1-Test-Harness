import os
import subprocess

files_directory = "test"
files = os.listdir(files_directory)

def wc_test(file_path):
    result = subprocess.check_output(['python', os.path.join('program_files','wc.py'), file_path], universal_newlines=True)
    return (result.strip())

def run_tests():
    global files_directory
    input_files = [file for file in files if file.endswith(".in") and "wc" in file]

    for file in input_files:
        file_path = os.path.join(files_directory, file)
        output = wc_test(file_path)
        print(f"File: {file}, Output:\n{output}")

if __name__ == "__main__":
    run_tests()
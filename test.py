import os
import subprocess

files_directory = "test"
files = os.listdir(files_directory)

def wc():
    global files_directory, files
    input_files = [file for file in files if file.endswith(".in") and "wc" in file]
    output_files = [file for file in files if file.endswith(".out") and "wc" in file]

    for i in range(0, len(input_files)):
        file_path = os.path.join(files_directory, input_files[i])
        output = subprocess.check_output(['python', os.path.join('prog','wc.py'), file_path], universal_newlines=True)

        out_file = os.path.join(files_directory, output_files[i])
        with open(out_file) as f:
            expected_output = f.read()

        try:
            assert expected_output.strip() == output.strip()
        except AssertionError:
            print(f"Failed for: {input_files[i]}")
            continue

    ## WC Test-1 for arguments:
    exp_out_file = "test/wc.test_1.arg.out"
    with open (exp_out_file) as o:
        expected = o.read()

    arg_output = subprocess.check_output(['python', 'prog\wc.py', 'test\wc.test_1.in', 'test\wc.test_2.in'], universal_newlines=True)
    # print(f"Args:\n{expected}\n{arg_output}")
    # print("Success!")

    ## WC Test-2 for arguments:
    exp_out_file = "test\wc.test_2.arg.out"
    with open (exp_out_file) as o:
        expected = o.read()

    arg_output = subprocess.check_output(['python', 'prog\wc.py', 'test\wc.test_2.in', 'test\wc.test_3.in', '-wl'], universal_newlines=True)
    # print(f"Args:\n{expected}\n{arg_output}")
    # print("Success!")

def gron():
        global files_directory
        input_files = [file for file in files if file.endswith(".in") and "gron" in file]
        output_files = [file for file in files if file.endswith(".out") and "gron" in file]

        for i in range(0, len(input_files)):
            file_path = os.path.join(files_directory, input_files[i])
            output = subprocess.check_output(['python', os.path.join('prog','gron.py'), file_path], universal_newlines=True)
            out_file = os.path.join(files_directory, output_files[i])
            with open(out_file) as f:
                expected_output = f.read()
            # print(f"{i}:\n{expected_output}\n{output}")
            try:
                assert expected_output.strip() == output.strip()
            except AssertionError:
                print(f"Failed for: {input_files[i]}")
                continue

        ## GRON test-1 for arguments:
        exp_out_file = "test\gron.test_1.arg.out"
        with open (exp_out_file) as o:
            expected = o.read()

        arg_output = subprocess.check_output(['python', 'prog\gron.py', 'test\gron.test_1.in', '--obj', 'ho'], universal_newlines=True)
        # print(f"Args:\n{expected}\n{arg_output}")
        # print("Success!")

def csv():
    global files_directory
    input_files = [file for file in files if file.endswith(".in") and "sumcsv" in file]
    output_files = [file for file in files if file.endswith(".out") and "sumcsv" in file]

    arg_column = ["Population", "Price", "Quantity"]

    for i in range(0, len(input_files)):
        file_path = os.path.join(files_directory, input_files[i])
        output = subprocess.check_output(['python', os.path.join('prog','sumcsv.py'), file_path, arg_column[i]], universal_newlines=True)
        out_file = os.path.join(files_directory, output_files[i+1])
        with open(out_file) as f:
            expected_output = f.read()
        # print(f"{i}:\n{expected_output}\n{output}")
        try:
            assert expected_output.strip() == output.strip()
        except AssertionError:
            print(f"Failed for: {input_files[i]}")
            continue

    # SUMCSV test-1 for arguments:
    exp_out_file = "test\sumcsv.test_1.arg.out"
    with open (exp_out_file) as o:
        expected = o.read()

    arg_output = subprocess.check_output(['python', 'prog\sumcsv.py', 'test\sumcsv.test_1.in', 'GDP', '--colrange', '1:4'], universal_newlines=True)
    # print(f"Args:\n{expected}\n{arg_output}")
    print("Success!")    

def test_run():
    wc()
    gron()
    csv()


# if __name__ == "__main__":
#     test_run()
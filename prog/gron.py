import sys
import argparse
import json

def gron(data, parent="", open_dict=True, open_list=True, obj="json"):
    if isinstance(data, dict):
        if not parent:
            print(f"{obj} = {{}};")
        if open_dict and parent:
            print(f"{obj}.{parent} = {{}};")
        for key,value in data.items():
            new_parent = f"{parent}.{key}" if parent else key
            gron(value, new_parent, isinstance(value, dict), isinstance(value, list), obj)
    
    elif isinstance(data, list):
        if not parent:
            print(f"{obj} = {{}};")
        if open_list and parent:
            print(f"{obj}.{parent} = {{}};")
        for index, item in enumerate(data):
            new_parent = f"{parent}[{index}]"
            gron(item, new_parent, isinstance(item, dict), isinstance(item, list), obj)
    else:
        print(f"{obj}.{parent} = {json.dumps(data)};")

def main():
    parser = argparse.ArgumentParser(prog="gron", description="Prints JSON in more readable format.")
    parser.add_argument("filename", type=str, help="Provide the name of the file.")

    arguments = parser.parse_args()

    try:
        with open(arguments.filename) as file:
            json_data = json.load(file)
            gron(json_data)
    
    except Exception as e:
        sys.stderr.write(e)
        sys.exit(1)
    
    sys.exit(0)

if __name__ == "__main__":
    main()
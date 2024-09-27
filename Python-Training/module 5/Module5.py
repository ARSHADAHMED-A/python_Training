import os

def findfiles(directory):
    for root, _, files in os.walk(directory):
        for file in files:
            yield os.path.join(root, file)
if __name__== "_main_":
    directory = "/path/to/directory"
    for file_path in findfiles(directory):
        print(file_path)
        
import os
from importlib.metadata import files


def list_files(directory):
    files = os.listdir(directory)
    for file in files:
        print(file)
        
    
   
import sys

def print_long_lines(filenames):
    for filename in filenames:
        try:
            with open(filename, 'r') as file:
                for line in file:
                    if len(line) > 40:
                        print(line.strip())
        except FileNotFoundError:
            print(f"File {filename} not found.")
        except Exception as e:
            print(f"An error occurred while processing {filename}: {e}")


if __name__ == "_main_":
    filename = input('enter the filename')
    print_long_lines(filename)    
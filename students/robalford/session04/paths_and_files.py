import os


def print_the_paths():
    for item in os.listdir():
        print(os.path.abspath(item))


def copy_file(source, destination):
    with open(source, 'r') as old_file:
        source_contents = old_file.read()
    with open(destination, 'w') as new_file:
        new_file.write(source_contents)

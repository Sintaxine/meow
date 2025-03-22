import sys

def meow(filename):
    try:
        with open(filename, 'r') as f:
            for line in f:
                sys.stdout.write(line)
    except (FileNotFoundError, PermissionError) as e:
        sys.stderr.write(f"Error: {e}\n")
        exit(1)

def main():
    argv = sys.argv
    argc = len(argv) - 1

    if argc != 1:
        sys.stderr.write("Invalid usage: catcopy <filename>\n")
        exit(1)

    meow(argv[1])


import sys
from pygments import highlight
from pygments.lexers import get_lexer_for_filename
from pygments.formatters import TerminalFormatter

def meow(filename):
    try:
        with open(filename, 'r') as f:
            code = f.read()

        lexer = get_lexer_for_filename(filename)

        highlighted_code = highlight(code, lexer, TerminalFormatter())

        for line in highlighted_code.splitlines():
            sys.stdout.write(line + '\n')

    except (FileNotFoundError, PermissionError) as e:
        sys.stderr.write(f"Error: {e}\n")
        exit(1)

def main():
    argv = sys.argv
    argc = len(argv) - 1

    if argc != 1:
        sys.stderr.write("Invalid usage: meow <filename>\n")
        exit(1)

    meow(argv[1])


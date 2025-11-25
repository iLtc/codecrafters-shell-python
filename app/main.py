import sys
import os


def cmd_echo(params):
    print(" ".join(params))


def cmd_type(params):
    if params[0] in ['echo', 'exit', 'type']:
        print(f"{params[0]} is a shell builtin")
        return

    paths = os.environ.get('PATH', '').split(os.pathsep)

    for path in paths:
        full_path = os.path.join(path, params[0])
        if os.path.exists(full_path) and os.access(full_path, os.X_OK):
            print(f"{params[0]} is {full_path}")
            return

    print(f"{params[0]}: not found")


def main():
    while True:
        sys.stdout.write("$ ")

        inputs = input().split()

        if inputs[0] == "exit":
            break

        if inputs[0] == "echo":
            cmd_echo(inputs[1:])
            continue

        if inputs[0] == "type":
            cmd_type(inputs[1:])
            continue

        print(f"{inputs[0]}: command not found")


if __name__ == "__main__":
    main()

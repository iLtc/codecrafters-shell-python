import sys
import os
import subprocess


def find_command_path(command):
    paths = os.environ.get('PATH', '').split(os.pathsep)

    for path in paths:
        full_path = os.path.join(path, command)
        if os.path.exists(full_path) and os.access(full_path, os.X_OK):
            return full_path

    return None


def cmd_echo(params):
    print(" ".join(params))


def cmd_type(params):
    if params[0] in ['echo', 'exit', 'type', 'pwd']:
        print(f"{params[0]} is a shell builtin")
        return

    command_path = find_command_path(params[0])

    if command_path:
        print(f"{params[0]} is {command_path}")
        return

    print(f"{params[0]}: not found")


def cmd_pwd():
    print(os.getcwd())


def cmd_exec(params):
    command_path = find_command_path(params[0])

    if command_path:
        subprocess.run(params)
    else:
        print(f"{params[0]}: command not found")


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

        if inputs[0] == "pwd":
            cmd_pwd()
            continue

        cmd_exec(inputs)


if __name__ == "__main__":
    main()

import sys
import os
import subprocess


current_dir = os.getcwd()


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
    command = params[0]

    if command in ['echo', 'exit', 'type', 'pwd']:
        print(f"{command} is a shell builtin")
        return

    command_path = find_command_path(command)

    if command_path:
        print(f"{command} is {command_path}")
        return

    print(f"{command}: not found")


def cmd_pwd():
    print(current_dir)


def cmd_cd(params):
    global current_dir

    path = params[0]

    if path.startswith("/"):
        if os.path.isdir(path):
            current_dir = path
        else:
            print(f"{path}: No such file or directory")


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

        if inputs[0] == "cd":
            cmd_cd(inputs[1:])
            continue

        cmd_exec(inputs)


if __name__ == "__main__":
    main()

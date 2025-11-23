import sys


def main():
    while True:
        sys.stdout.write("$ ")

        command = input()

        if command.startswith("echo "):
            print(command[5:])
            continue

        if command == "exit":
            break

        print(f"{command}: command not found")


if __name__ == "__main__":
    main()

import argparse
import subprocess
import logging
import platform


def check_python():

    result = subprocess.run(
        ["python3", "--version"],
        capture_output=True,
        text=True
    )

    print(result.stdout)

def check_git():
    
    result = subprocess.run(
        ["git", "--version"],
        capture_output=True,
        text=True
    )

    print(result.stdout)

def check_system():

    print("System:", platform.system())
    print("Machine:", platform.machine())
    print("Processor:", platform.processor())


def main():

    parser = argparse.ArgumentParser(description="Devops System Checker")

    parser.add_argument("--check_python", action="store_true")
    parser.add_argument("--check_git", action="store_true")
    parser.add_argument("--check_system", action="store_true")

    args = parser.parse_args()

    if args.check_python:
        check_python()
    
    if args.check_git:
        check_git()

    if args.check_system:
        check_system()


if __name__ == "__main__":
    main()

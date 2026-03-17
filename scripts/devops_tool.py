"""CLI tool for checking installed development tools and system information."""

import argparse
import subprocess
import platform


def check_python() -> None:
    """Print the installed Python version."""
    result = subprocess.run(["python3", "--version"], capture_output=True, text=True)
    print(result.stdout.strip())


def check_git() -> None:
    """Print the installed Git version."""
    result = subprocess.run(["git", "--version"], capture_output=True, text=True)
    print(result.stdout.strip())


def check_system() -> None:
    """Print system information."""
    print(f"System:    {platform.system()}")
    print(f"Machine:   {platform.machine()}")
    print(f"Processor: {platform.processor()}")


def main() -> None:
    parser = argparse.ArgumentParser(description="DevOps System Checker")
    parser.add_argument("--python", action="store_true", help="Check Python version")
    parser.add_argument("--git", action="store_true", help="Check Git version")
    parser.add_argument("--system", action="store_true", help="Check system info")

    args = parser.parse_args()

    if args.python:
        check_python()
    if args.git:
        check_git()
    if args.system:
        check_system()


if __name__ == "__main__":
    main()

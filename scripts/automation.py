"""Automation script that inspects the project directory and runs shell commands."""

import os
import subprocess
import logging

logging.basicConfig(level=logging.INFO)


def check_project_directory() -> None:
    """Log the current working directory and its contents."""
    current_dir = os.getcwd()
    logging.info(f"Current directory: {current_dir}")

    for file in os.listdir(current_dir):
        logging.info(file)


def run_shell_commands() -> None:
    """Run and display output of common development tool checks."""
    logging.info("Running shell commands")

    commands = [
        ["python3", "--version"],
        ["git", "--version"],
        ["git", "status"],
    ]

    for command in commands:
        result = subprocess.run(command, capture_output=True, text=True)
        print(result.stdout)


def main() -> None:
    logging.info("Starting automation script...")
    check_project_directory()
    run_shell_commands()
    logging.info("Automation script completed")


if __name__ == "__main__":
    main()

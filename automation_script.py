import os
import subprocess
import logging

logging.basicConfig(level=logging.INFO)


def check_project_directory():

    logging.info("Checking current directory")

    current_dir = os.getcwd()

    logging.info(f"Current directory: {current_dir}")

    files = os.listdir(current_dir)

    logging.info("Project files:")

    for file in files:
        logging.info(file)



def run_shell_command():

    logging.info("Running shell commands")

    commands = [
        ["python3", "--version"],
        ["git", "--version"],
        ["git", "status"]
    ]

    for command in commands:

        result = subprocess.run(
            command,
            capture_output=True,
            text=True
        )

        print(result.stdout)


def main():

    logging.info("Starting automation script...")

    check_project_directory()

    run_shell_command()

    logging.info("Automation script completed")


if __name__ == "__main__":
    main()
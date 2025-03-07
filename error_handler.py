import subprocess

def run_command(command, log_file_path):
    with open(log_file_path, "w") as log_file:
        result = subprocess.run(command, shell=True, stdout=log_file, stderr=log_file)
        if result.returncode != 0:
            print(f"Error occurred. See log file: {log_file_path}")
            exit(1)

import subprocess

def bad():
    subprocess.call("ls", shell=True)
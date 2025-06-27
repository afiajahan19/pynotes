import sys
import subprocess

def get_local_pyinfo():
    return f'conda env: {sys.prefix.split("/")[-1]}; pyv: {sys.version}'

def ps2(package_name):
    result = subprocess.run(
        ["pip", "show", package_name],
        capture_output=True,
        text=True
    )
    return result.stdout

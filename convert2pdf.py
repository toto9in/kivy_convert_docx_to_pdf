import subprocess
import sys
import os

# Get the directory of the current file
dir_path = os.path.dirname(os.path.realpath(__file__))

# Build the path to app.py
app_path = os.path.join(dir_path, 'app.py')

# Run the script using the current Python interpreter
subprocess.call([sys.executable, app_path])
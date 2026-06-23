import subprocess, sys, pathlib
subprocess.run([sys.executable, str(pathlib.Path(__file__).with_name('validate_v140.py'))], check=True)

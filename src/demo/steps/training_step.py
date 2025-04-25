__all__ = ['train']

from zenml import step

import sys
import os
import site
import importlib
print("=== Initial State ===")
print("sys.path:")
for p in sys.path:
    print(f"  {p}")

print("\nChecking .pth files:")
for site_dir in site.getsitepackages():
    if os.path.exists(site_dir):
        for file in os.listdir(site_dir):
            if file.endswith('.pth'):
                pth_path = os.path.join(site_dir, file)
                print(f"\nContents of {pth_path}:")
                try:
                    with open(pth_path, 'r') as f:
                        print(f.read())
                except Exception as e:
                    print(f"Error reading .pth file: {e}")

print("\n=== Checking /app/code/src/demo directory ===")
try:
    import subprocess
    ls_output = subprocess.check_output(["ls", "-la", "/app/code/src/demo/"]).decode("utf-8")
    print("Directory listing of /app/code/src/demo/:")
    print(ls_output)
except Exception as e:
    print(f"Error running ls command: {e}")

print("\n=== Checking __init__.py ===")
init_path = "/app/code/src/demo/__init__.py"
try:
    if os.path.exists(init_path):
        print(f"Contents of {init_path}:")
        with open(init_path, 'r') as f:
            print(f.read())
    else:
        print(f"File {init_path} does not exist")
except Exception as e:
    print(f"Error reading __init__.py: {e}")


print("\nsite-packages directories:")
for p in site.getsitepackages():
    print(f"  {p}")

print("\nCurrently loaded modules:")
for name, module in sys.modules.items():
    if 'demo' in name:
        print(f"  {name}: {module}")

print("\n=== Attempting to import demo ===")
try:
    import demo
    print(f"Demo module location: {demo.__file__}")
except ImportError as e:
    print(f"Import failed: {e}")

print("\n=== Clearing caches and trying again ===")
if 'demo' in sys.modules:
    print("Removing demo from sys.modules")
    del sys.modules['demo']

print("Invalidating import caches")
importlib.invalidate_caches()
site.main()

print("\n=== Final State ===")
print("sys.path:")
for p in sys.path:
    print(f"  {p}")

# verify thet file /app/code/src/demo/training.py exists
import os
if os.path.exists("/app/code/src/demo/training.py"):
    print("File /app/code/src/demo/training.py exists")
else:
    print("File /app/code/src/demo/training.py does not exist")

from demo.training import train_model

@step
def train():
    train_model()

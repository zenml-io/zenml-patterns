import importlib
import sys
import site
import os

print("=== Initial State ===")
print("sys.path:")
for p in sys.path:
    print(f"  {p}")

print("\nsite-packages directories:")
for p in site.getsitepackages():
    print(f"  {p}")

# Check for .pth files
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

print("\n=== Final State ===")
print("sys.path:")
for p in sys.path:
    print(f"  {p}")

print("\nCurrently loaded modules:")
for name, module in sys.modules.items():
    if 'demo' in name:
        print(f"  {name}: {module}")

print("\n=== Trying final import ===")
try:
    import demo
    print(f"Demo module location: {demo.__file__}")
except ImportError as e:
    print(f"Import failed: {e}") 
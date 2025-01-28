import subprocess
import sys

# List of required packages
required_packages = [
    "tkinter"  # tkinter is part of the standard library, but we can check if it's available
]

def install_package(package):
    """Install a package using pip."""
    try:
        print(f"Checking for {package}...")
        __import__(package)  # Try importing the package
    except ImportError:
        print(f"{package} not found. Installing...")
        subprocess.check_call([sys.executable, "-m", "pip", "install", package])

def update_pip():
    """Update pip to the latest version."""
    print("Updating pip...")
    subprocess.check_call([sys.executable, "-m", "pip", "install", "--upgrade", "pip"])

def check_tkinter():
    """Check if tkinter is available."""
    try:
        import tkinter
        print("tkinter is available.")
    except ImportError:
        print("tkinter is not available. Please install it via your system's package manager.")

# Update pip first
update_pip()

# Check for tkinter
check_tkinter()

# Install required packages
for package in required_packages:
    install_package(package)

print("All required packages are installed and pip is updated.")

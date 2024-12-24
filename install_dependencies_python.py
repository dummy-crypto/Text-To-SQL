import subprocess
import os

# Function to install system packages
def install_system_packages():
    if os.path.exists("packages.txt"):
        subprocess.run("sudo apt update && sudo apt upgrade -y", shell=True)
        with open("packages.txt", "r") as file:
            packages = file.readlines()
            for package in packages:
                subprocess.run(f"sudo apt install -y {package.strip()}", shell=True)
    print("✅ System packages installed")

# Function to install Python packages
def install_python_dependencies():
    if os.path.exists("requirements.txt"):
        subprocess.run("pip3 install --user -r requirements.txt", shell=True)
    subprocess.run("pip3 install --user streamlit", shell=True)
    print("✅ Python packages installed")

# Function to install VSCode extensions
def install_vscode_extensions():
    extensions = [
        "ms-python.python",
        "ms-python.vscode-pylance"
    ]
    for ext in extensions:
        subprocess.run(f"code --install-extension {ext}", shell=True)
    print("✅ VSCode extensions installed")

# Function to run the Streamlit app
def run_streamlit_app():
    command = "streamlit run final.py --server.enableCORS false --server.enableXsrfProtection false"
    subprocess.run(command, shell=True)

# Execute all steps
install_system_packages()
install_python_dependencies()
install_vscode_extensions()
run_streamlit_app()

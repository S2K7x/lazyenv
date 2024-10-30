import os
import subprocess
import sys
import argparse
import venv

def create_venv(venv_path):
    """Creates a virtual environment at the specified path."""
    venv.create(venv_path, with_pip=True)
    print(f"Virtual environment created at {venv_path}")

def activate_venv_command(venv_path):
    """Returns the activation command for the virtual environment based on OS."""
    if os.name == 'nt':  # Windows
        return f"{os.path.join(venv_path, 'Scripts', 'activate')}.bat"
    else:  # Unix/Linux/MacOS
        return f"source {os.path.join(venv_path, 'bin', 'activate')}"

def install_requirements(venv_path, requirements_file):
    """Installs the requirements in the given file within the virtual environment."""
    pip_executable = os.path.join(venv_path, 'Scripts' if os.name == 'nt' else 'bin', 'pip')
    try:
        subprocess.check_call([pip_executable, 'install', '-r', requirements_file])
        print(f"Requirements from {requirements_file} installed successfully.")
    except subprocess.CalledProcessError as e:
        print("An error occurred while installing the requirements.")
        sys.exit(e.returncode)

def main():
    parser = argparse.ArgumentParser(description="Create and use a virtual environment, then install requirements.")
    parser.add_argument('requirements_file', help="Path to the requirements file")
    parser.add_argument('--venv-name', default="my_venv", help="Name for the virtual environment directory (default: 'my_venv')")
    args = parser.parse_args()

    # Path for the virtual environment directory
    venv_path = os.path.join(os.getcwd(), args.venv_name)

    # Step 1: Create the virtual environment
    create_venv(venv_path)

    # Step 2: Install requirements from the provided file
    install_requirements(venv_path, args.requirements_file)

    # Step 3: Output the activation command
    activation_command = activate_venv_command(venv_path)
    print("\nTo activate the virtual environment, use the following command:")
    print(activation_command)

if __name__ == "__main__":
    main()

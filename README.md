# LazyEnv

**LazyEnv** is a Python script designed to automate the creation and management of virtual environments. With **LazyEnv**, you can quickly create a virtual environment, install dependencies from a requirements file, and receive an easy-to-use activation command for your virtual environment—all in a single step!

## Features

- **Automated Virtual Environment Creation**: Specify a custom name or use the default.
- **Dependency Installation**: Install packages from a provided requirements file.
- **Cross-Platform Activation**: Outputs the correct command to activate the virtual environment on Windows, Linux, or MacOS.

## Installation

Clone the repository or download `lazyenv.py`:

```bash
git clone https://github.com/S2K7x/lazyenv.git
cd lazyenv
```

## Usage

Run `lazyenv.py` with the path to your requirements file. You can optionally specify a name for your virtual environment directory.

### Command-Line Arguments

- `requirements_file` (positional): Path to the `requirements.txt` file with the dependencies you want to install.
- `--venv-name` (optional): Name for the virtual environment directory. Defaults to `my_venv`.

### Examples

1. **Basic Usage**

   ```bash
   python lazyenv.py path/to/requirements.txt
   ```

   This will:
   - Create a virtual environment named `my_venv` in the current directory.
   - Install all packages listed in `path/to/requirements.txt`.
   - Output the command to activate the environment.

2. **Custom Virtual Environment Name**

   ```bash
   python lazyenv.py path/to/requirements.txt --venv-name custom_env
   ```

   This will:
   - Create a virtual environment named `custom_env`.
   - Install packages from `path/to/requirements.txt`.
   - Output the activation command for `custom_env`.

## Example Output

After running the script, you will see output similar to:

```bash
Virtual environment created at /path/to/custom_env
Requirements from requirements.txt installed successfully.

To activate the virtual environment, use the following command:
source /path/to/custom_env/bin/activate  # Linux/MacOS
```

Or, on Windows:

```cmd
To activate the virtual environment, use the following command:
path\to\custom_env\Scripts\activate.bat
```

## Requirements

- Python 3.6+
- `requirements.txt` file with dependencies (optional)

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Author

Developed by **[Your Name/Username]**.

## Contributions

Feel free to open an issue or submit a pull request with improvements and bug fixes.

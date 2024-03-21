#!/bin/bash

echo "-----------------------------------------------------------"
echo "Building virtual environment for Python version xxx"
echo "This environment should be used only for general tasks like mkdocs. Custom projects should have their own virtual environment."

# Define the Python version
python_version="3.11.5"  # Replace xxx with the desired version, e.g., "3.8.5"

# Check if pyenv is installed
if ! command -v pyenv &> /dev/null; then
    echo "-----------------------------------------------------------"
    echo "pyenv could not be found"
    echo "Please install pyenv first"
    echo " "
    exit 1
fi

# Check if the desired Python version is installed
if pyenv versions | grep -q "${python_version}"; then
    echo "-----------------------------------------------------------"
    echo "Python version ${python_version} is already installed."
else
    echo "-----------------------------------------------------------"
    echo "Installing Python version ${python_version}."
    pyenv install "${python_version}"
    if [ $? -ne 0 ]; then
        echo "Failed to install Python version ${python_version}."
        exit 1
    fi
fi

# Set the desired Python version as the local version
pyenv local ${python_version}

# Find path to python_version
python_path=$(pyenv which python)

# Print path to python_version
echo "Python path: ${python_path}"

# Define the environment directory
env_dir="venv_local"  # Replace with your desired environment directory path

# Create a new virtual environment using the specified Python version
${python_path} -m venv "${env_dir}"

if [ $? -eq 0 ]; then
    echo "-----------------------------------------------------------"
    echo "Virtual environment created successfully in ${env_dir}."
    echo "Python version: $(python --version)"
else
    echo "-----------------------------------------------------------"
    echo "Failed to create virtual environment in ${env_dir}."
    exit 1
fi

# Activate the virtual environment
source "${env_dir}/bin/activate"
if [ $? -ne 0 ]; then
    echo "-----------------------------------------------------------"
    echo "Failed to activate the virtual environment."
    exit 1
fi

#print where is script running from
echo "-----------------------------------------------------------"
echo "Script running from: $(pwd)"

# Install packages from requirements.txt
requirements_file="requirements.txt"  # Replace with your actual requirements file path
if [ -f "${requirements_file}" ]; then
    echo "-----------------------------------------------------------"
    echo "Installing packages from ${requirements_file}...."
    pip install -r "${requirements_file}"
    if [ $? -eq 0 ]; then
        echo "Packages from ${requirements_file} installed successfully."
    else
        echo "Failed to install packages from ${requirements_file}."
        exit 1
    fi
else
    echo "-----------------------------------------------------------"
    echo "Requirements file ${requirements_file} does not exist."
    exit 1
fi

#!/bin/bash

# Exit immediately if a command exits with a non-zero status.
set -e

# Update the package list
sudo apt-get update

# Install Python and pip if they are not already installed
sudo apt-get install -y python3 python3-pip

# Install virtualenv for creating isolated Python environments
sudo pip3 install virtualenv

# Create a virtual environment in the current directory
virtualenv -p /usr/bin/python3 venv

# Activate the virtual environment
source venv/bin/activate

# Install django
pip install django

# Install Pillow (Python Imaging Library)
pip install Pillow

# Install Django REST framework
pip install djangorestframework

# Install Simple JWT for token-based authentication
pip install djangorestframework-simplejwt
# pip install some-other-package if needed

# Migrations
./manage.py makemigrations
./manage.py migrate

echo "Environment setup and package installation complete."

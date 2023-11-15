#!/bin/bash

# Activate the virtual environment
source venv/bin/activate

# Navigate to the directory where manage.py is located
cd /home/ubuntu/Documents/petpal

# Start the Django development server
./manage.py runserver
import os

# Define the directory and file paths
directory = "engine"
init_file = os.path.join(directory, "__init__.py")
additional_file = os.path.join(directory, "my_file.py")

# Create the directory if it doesn't exist
if not os.path.exists(directory):
    os.makedirs(directory)

# Create the __init__.py file
with open(init_file, 'w') as f:
    pass  # This creates an empty file

# Create the additional file
with open(additional_file, 'w') as f:
    pass  # This creates an empty file

print(f"Directory '{directory}' and files '{init_file}', '{additional_file}' created successfully.")

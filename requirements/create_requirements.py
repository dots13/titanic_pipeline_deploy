# Define the input and output file paths
input_file_path = "requirements_row.txt"  # Replace with your input file path
output_file_path = "requirements.txt"

# Open the input file and read the lines
with open(input_file_path, "r") as file:
    lines = file.readlines()

# Prepare a list to hold formatted package strings
requirements = []

# Loop through each line to extract package names and versions
for line in lines:
    # Skip comment lines and lines without package specifications
    if line.startswith("#") or '=' not in line:
        continue
    
    # Split the line on '=' to get the package name and version
    package_info = line.strip().split('=')
    package_name = package_info[0]
    package_version = package_info[1].split('=')[0]  # Get the version part before the second '='

    # Split the version to get major, minor, and patch parts
    version_parts = package_version.split('.')
    
    # Ensure we can access the major version (handle if not enough parts)
    if len(version_parts) > 0:
        major_version = int(version_parts[0])  # Convert to integer
        next_major_version = major_version + 1  # Increment major version
        
        # Create the formatted requirement string
        requirement = f"{package_name}>={package_version},<{next_major_version}.0.0"  # This assumes major version increment
        requirements.append(requirement)

# Write the formatted requirements to the output file
with open(output_file_path, "w") as output_file:
    for req in requirements:
        output_file.write(req + "\n")

print(f"Requirements have been written to {output_file_path}")

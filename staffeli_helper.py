import subprocess as sp
import os
import sys
import re as regex

print("\nThis script will help you download or upload assignments using the Staffeli CLI.")
print("Make sure you have the Staffeli CLI installed and that you are in the correct environment.")
print("______________________________________________________________________________________________\n\n")

yaml_files = [f for f in os.listdir() if f.endswith(".yml") or f.endswith(".yaml")]
if not yaml_files:
    print("No YAML files found in the working directory, either use an existing template or create your own.")
    sys.exit(1)

print("Choose your grading template: ")
for i, file in enumerate(yaml_files):
    print(f"{i}. {file}")

template_choice = int(input(f"Choose a grading template [0-{len(yaml_files)-1}]: "))
template = yaml_files[template_choice]

print("Choose your distribution template: ")
for i, file in enumerate(yaml_files):
    print(f"{i}. {file}")

distribution_choice = int(input(f"Choose a distribution template [0-{len(yaml_files)-1}]: "))
distribution = yaml_files[distribution_choice]

pattern = r"^ass\d+dir$"
assignment_directory_name = input("Enter the assignment directory name (use ass1dir for assignment 1 etc.): ")
while not regex.match(pattern, assignment_directory_name):
    print("\nError: The assignment directory name must follow the format ass{number}dir.")
    print("Try again following the correct format.\n")
    assignment_directory_name = input("Enter the assignment directory name (use ass1dir for assignment 1 etc.): ")


commands = {
    "download": f"python /Users/anderspersson/staffeli_nt/staffeli_nt download 77304 {template} {assignment_directory_name} --select-ta {distribution}",
    "test_upload": f"python /Users/anderspersson/staffeli_nt/staffeli_nt upload {template} {assignment_directory_name} --step",
    "live_upload": f"python /Users/anderspersson/staffeli_nt/staffeli_nt upload {template} {assignment_directory_name} --live"
}

options = ["Download assignments", "Upload assignments (Test)", "Upload assignments (Live)"]

print("Choose an option:")
for i, option in enumerate(options):
    print(f"{i}. {option}")

choice = int(input(f"Enter the number corresponding to your choice [0-{len(options)-1}]: "))

if choice == 0:
    command = commands["download"]
elif choice == 1:
    command = commands["test_upload"]
elif choice == 2:
    command = commands["live_upload"]
else:
    print("Invalid choice. Exiting.")
    sys.exit(1)

print(f"Executing command: {command}")

sp.run(command, shell=True, executable="/bin/bash")

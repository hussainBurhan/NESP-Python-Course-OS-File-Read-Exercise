# Import the os module to interact with the operating system
import os

# Define a function named 'search_file' that takes an 'address' and a 'file' name as arguments
def search_file(address, file):
    # Use os.walk to get a list of all files and directories in 'address' and its subdirectories
    list_os = os.walk(address)

    # Iterate through the list of files and directories
    for root, direct, files in list_os:
        for j in files:
            # Check if the target 'file' exists in the list of files
            if file in j:
                print("Yes the file exists")

# Call the 'search_file' function with the specified 'address' and 'file' name
search_file('E:\\GitHub Python Projects\\OS File Read Exercise', 'main.py')

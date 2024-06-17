import os


def rename_files_sequentially(folder_path):
    # Get a list of all files in the directory
    files = os.listdir(folder_path)

    # Sort files to ensure they are renamed in a consistent order
    files.sort()

    # Iterate over the files and rename them
    for index, filename in enumerate(files):
        # Split the filename into name and extension
        name, ext = os.path.splitext(filename)

        # Construct the new filename
        new_name = f"{index + 1}{ext}"

        # Get the full file paths
        old_file = os.path.join(folder_path, filename)
        new_file = os.path.join(folder_path, new_name)

        # Rename the file
        os.rename(old_file, new_file)
        print(f"Renamed: {old_file} -> {new_file}")


# Path to the folder containing the files to rename
folder_path = 'filepath'

# Call the function to rename the files
rename_files_sequentially(folder_path)

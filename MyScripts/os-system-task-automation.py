import os
import shutil

def copy_file(src, dest):
    """
    Copy a file from source to destination.

    :param src: Source file path
    :param dest: Destination file path
    :return: None
    """
    try:
        shutil.copy(src, dest)
        print(f"File '{src}' copied to '{dest}' successfully.")
    except Exception as e:
        print(f"Error copying file '{src}' to '{dest}': {e}")

# Directory paths
dir_src = '/path/to/source/directory'
dir_dest = '/path/to/destination/directory'

# Create destination directory if it doesn't exist
if not os.path.exists(dir_dest):
    os.makedirs(dir_dest)

# List of files to be copied
arquivos = ['file1.txt', 'file2.txt']

# Copy files to the destination directory
for file_name in arquivos:
    src_file = os.path.join(dir_src, file_name)
    dest_file = os.path.join(dir_dest, file_name)
    copy_file(src_file, dest_file)

print("Files copied successfully!")
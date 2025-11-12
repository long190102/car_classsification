import os
import shutil

def copy_all_files(src_folder, dst_folder):
    """
    Copy all files from src_folder to dst_folder.

    Parameters:
        src_folder (str): Source directory path.
        dst_folder (str): Destination directory path.
    """
    # Ensure source exists
    if not os.path.exists(src_folder):
        print(f"❌ Source folder not found: {src_folder}")
        return

    # Create destination if it doesn't exist
    os.makedirs(dst_folder, exist_ok=True)

    # Iterate and copy files
    for filename in os.listdir(src_folder):
        src_path = os.path.join(src_folder, filename)
        dst_path = os.path.join(dst_folder, filename)

        if os.path.isfile(src_path):
            shutil.copy2(src_path, dst_path)  # copy2 preserves metadata
            print(f"📁 Copied: {filename}")

    print(f"✅ All files copied from '{src_folder}' to '{dst_folder}'")
path = 'Thuy_crop_data(final_data)'

makes = os.listdir(path)
carname = []
for make in makes:
    copypaths = os.listdir(path + '/' + make)

    for copypath in copypaths:
        src_folder = path + '/' + make + '/' + copypath
        dst_folder = 'cars_train/cars_train'
        copy_all_files(src_folder, dst_folder)
import os
import shutil

def ensure_clean_directory(path):
    if os.path.exists(path):
        shutil.rmtree(path)
        os.mkdir(path)
    else:
        os.mkdir(path)
    return path

def copy_directory_to_another(source_path, destination_path):
    source_path_list = os.listdir(source_path)
    for name in source_path_list:
        full_source_path = os.path.join(source_path, name)
        full_destination_path = os.path.join(destination_path, name)
        if os.path.isfile(full_source_path):
            shutil.copy(full_source_path, full_destination_path)
        else:
            ensure_clean_directory(full_destination_path)
            copy_directory_to_another(full_source_path, full_destination_path)
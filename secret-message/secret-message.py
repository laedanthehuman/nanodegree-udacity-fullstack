import os

def rename_files():
    # (1) get file names from a folder
    dir_path = os.path.dirname(os.path.realpath(__file__))
    prank_dir = dir_path + "/prank"
    file_list = os.listdir(prank_dir)

    os.chdir(prank_dir)
    #(2) for each file, rename filename
    for filename in file_list:
        table = filename.maketrans("0123456789", "          ")
        new_filename = filename.translate(table).strip()
        print("old name file: ", filename, " new filename: ", new_filename)
        os.rename(filename, new_filename)


rename_files()

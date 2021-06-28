import pathlib
from pathlib import Path
import contextlib
import os


def file_exists(file_path): return Path(file_path).exists()


def unzip_file(target_dir, filename):
    from zipfile import ZipFile
    with ZipFile(filename,"r") as zipped_file:  # open in read mode
        zipped_file.printdir()
        print('extracting files from zip')
        zipped_file.extractall(target_dir)
        print('done unzipping')


def zip_file(target_dir, target_filename):
    import zipfile
    print("creating zip file")
    with zipfile.ZipFile(target_filename,"r") as zip_f:
        zip_f.write(target_filename)


def get_all_file_paths(directory):
    file_paths = []
    # crawling through directory and subdirectories
    for root, directories, files in os.walk(directory):
        for filename in files:
            # join the two strings in order to form the full filepath.
            filepath = os.path.join(root, filename)
            file_paths.append(filepath)
    # returning all file paths
    return file_paths


def zip_folder(target_folder: str, zip_file_to_create: str):
    from zipfile import ZipFile
    file_paths = get_all_file_paths(target_folder)
    print('Following files will be zipped:')
    for file_name in file_paths:
        print(file_name)
    with ZipFile(zip_file_to_create, 'w') as zip_f:
        # writing each file one by one
        for file in file_paths:
            zip_f.write(file)
    print('All files zipped successfully!')


def get_zip_file_info(target_file):
    # importing required modules
    from zipfile import ZipFile
    import datetime
    # specifying the zip file name
    file_name = target_file
    # open zip file in READ mode
    with ZipFile(file_name, 'r') as zip_f:
        for info in zip_f.infolist():
            print(info.filename)
            print('\tModified:\t' + str(datetime.datetime(*info.date_time)))
            print('\tSystem:\t\t' + str(info.create_system) + '(0 = Windows, 3 = Unix)')
            print('\tZIP version:\t' + str(info.create_version))
            print('\tCompressed:\t' + str(info.compress_size) + ' bytes')
            print('\tUncompressed:\t' + str(info.file_size) + ' bytes')


# https://docs.python.org/3/library/bz2.html
def decompress_bz2_file(input_file, output_file):
    """mode argument can be 'r', 'rb', 'w', 'wb', 'x', 'xb', 'a' or 'ab' for binary mode,
    or 'rt', 'wt', 'xt', or 'at' for text mode. default is 'rb' """
    import bz2
    import shutil

    with bz2.BZ2File(input_file) as zipped_file:
        with open(output_file, 'w') as unzipped_file:
            shutil.copyfileobj(zipped_file, unzipped_file)


def compress_bz2_file(source_file, output_file, compression_lvl=9):
    import bz2
    if 1 <= compression_lvl <= 9:
        with open(source_file, 'rb') as data:
            tar_bz2_contents = bz2.compress(data.read(), compresslevel=compression_lvl)
    else:
        raise ValueError("compression level has to be between 1 and 9")


# concatenate_files_in_list(text_files_list, final_file, 'latin-1', True)
def concatenate_files_in_list(file_list, output_file, encode_in='utf-8', is_small=False, use_shutil=False):
    # don't forget to specify target folder when opening files!
    # todo: check if file was created already
    encoding_format = encode_in
    print(f"target file -> {output_file}")
    readmode = ('rb' if use_shutil else 'r')
    writemode = ('wb' if use_shutil else 'w+')
    with open(output_file, writemode) as finaltext:
        for file_name in file_list:
            print(f"currently appending file: {file_name}")
            with open(file_name, readmode, encoding=encoding_format) as file_currently_opened:
                if use_shutil:
                    import shutil
                    shutil.copyfileobj(file_name, finaltext)
                elif is_small:
                    finaltext.write(file_currently_opened.read())
                elif not is_small:
                    for line in file_currently_opened:
                        finaltext.write(line)


def add_files_from_folder_to_list(filetype, folder_target='./'):
    folder = set_folder(folder_target)
    print(folder)
    print(f"getting files from {folder} of type {filetype} ...")
    all_files = []
    for path, dirs, files in os.walk(folder):
        for filename in files:
            if filename.endswith('.txt'):
                full_path = os.path.join(path,filename)
                all_files.append(full_path)
    with contextlib.suppress(Exception):
        raise RuntimeError('something went wrong')
    return all_files


def set_folder(folder_dir):
    isdir = Path(folder_dir)
    if not isdir:
        raise Exception(f"folder you're trying to set is invalid -> {folder_dir}")
    absolute_path = isdir.resolve()
    return absolute_path


def test_files_in_list(file_list: []):
    print("testing files in list... ")
    for file in file_list:
        if not Path(file).exists():
            print(f"oops: {file} doesn't seem to exist")

def initiate_numpy(console_width=640):
    # https://numpy.org/doc/stable/reference/generated/numpy.set_printoptions.html
    try:
        import numpy as np
        np.set_printoptions(linewidth=console_width)
        return np
    except ImportError:
        print("numpy not installed")

def initiate_pandas(max_rows=10, max_cols=10, console_width=640):
    try:
        import pandas as pd
        pd.set_option('display.max_columns', max_cols)
        pd.set_option('display.max_rows', max_rows)
        pd.set_option('display.width', console_width)  # make output in console wider
        return pd
    except ImportError:
        print("pandas not installed")


import os
import glob
from subprocess import CalledProcessError, check_call


def check_files(user_input):
    """
    Checks to make sure given directory is a valid directory.
    If directory exists, returns list of .fit or .fits files.
    """
    file_ext = ['*.fit*', '*.FIT*']
    data_files = []
    working_dir = os.path.exists(user_input)

    if working_dir:
        os.chdir(user_input)
        if glob.glob('*.gz*'):
            try:
                check_call('gunzip *.gz', shell=True)
            except CalledProcessError:
                pass
        for files in file_ext:
            data_files += glob.glob(files)
        if not data_files:
            print('Input directory contains no .fit(s) or .FIT(S) files.  Please enter another directory.')
            return False
        print(data_files)
        return data_files
    else:
        print('Invalid directory. Please try again.')
        return False


def rm_spaces(list1):
    """
    Removes all whitespace from members of a list (assuming list contains only str objects).

    :param list1: input list where are whitespace is replaced with '_'
    :return: modified list1
    """
    if len(list1) > 0:
        for i in range(len(list1)):
            if ' ' in list1[i]:
                j = list1[i].replace(' ', '_')
                os.rename(list1[i], j)
                list1.pop(i)
                list1.insert(i, j)
        return list1
    else:
        print('Directory contains no .fit(s) or .FIT(s) files.')
        return False


def get_files():
    """
    Decompress all FIT.gz files is they exists and returns list of all fit/FIT files in active directory.

    :return: fits+FITS as a list
    """
    try:
        if glob.glob('*.gz*'):
            check_call('gunzip *FIT.gz', shell=True)
            check_call('gunzip *fit.gz', shell=True)
            fits = glob.glob('*.fit*')
            FITS = glob.glob('*.FIT*')
            no_space = rm_spaces(list1=fits + FITS)
            return no_space
    except CalledProcessError:
        raise
    try:
        if glob.glob('*.fit*') or glob.glob('*FIT'):
            fits = glob.glob('*.fit*')
            FITS = glob.glob('*.FIT*')
            no_space = rm_spaces(list1=fits + FITS)
            return no_space
    except CalledProcessError:
        raise

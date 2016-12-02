import os
import pathlib
import shutil
import stat
from distutils.dir_util import copy_tree


# import getpass
# USER = getpass.getuser()


def ensure_dir_exists(path, verbose=False):
    path = pathlib.Path(path)
    if not path.parent.exists():
        ensure_dir_exists(path=path.parent.absolute())

    if not path.is_dir():
        if verbose:
            print('creating with permissions:')
        path.mkdir()
        try:
            # shutil.chown(str(path), group='lab')
            os.chmod(str(path), stat.S_IRWXU | stat.S_IRWXG)
        except PermissionError:
            print(
                "WARNING: It was not possible to change the permission to the following files: \n"
                + path + "\n")
        if verbose:
            print('made outpath: {p}'.format(p=path))


def change_file_permissions(file_path):
    if not isinstance(file_path, pathlib.Path):
        file_path = pathlib.Path(file_path)
    if not file_path.is_file():
        print('path does not exist')
        return
    try:
        # shutil.chown(str(file_path), group='lab')
        os.chmod(str(file_path), stat.S_IRWXU | stat.S_IRWXG)
    except:
        print(
            "WARNING: It was not possible to change the permission to the following files: \n"
            + str(file_path))


def copy_file(input_path, output_path):
    ensure_dir_exists(path=output_path.parent)
    shutil.copy(str(input_path), str(output_path))
    change_file_permissions(output_path)


def copy_dir(input_path, output_path):
    ensure_dir_exists(path=output_path.parent)
    copy_tree(src=str(input_path), dst=str(output_path))

def move(src, dst):
    shutil.move(src, dst)

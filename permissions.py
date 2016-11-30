import shutil
import os
import stat
import pathlib
"""
Additional Help


stat.S_IRWXU -- mask for file owner permissions
stat.S_IRWXG --  mask for file group permissions
stat.S_IROTH -- others have read permissions
stat.S_IXOTH -- others have exicute permissions
"""


def ensure_dir_permissions(path):
    path = pathlib.Path(path)
    if not path.parent.exists():
        ensure_dir_permissions(path=path.parent.absolute())

    if not path.is_dir():
        print('creating with permissions:')
        path.mkdir()
        try:
            shutil.chown(str(path), group='lab')
            os.chmod(str(path), stat.S_IRWXU | stat.S_IRWXG)
        except PermissionError:
            print(
                "WARNING: It was not possible to change the permission to the following files: \n"
                + path + "\n")
        print('made outpath: {p}'.format(p=path))


def change_file_permissions(file_path):
    if not isinstance(file_path, pathlib.Path):
        file_path = pathlib.Path(file_path)
    if not file_path.is_file():
        print('path does not exist')
        return
    try:
        shutil.chown(str(file_path), group='lab')
        os.chmod(str(file_path), stat.S_IRWXU | stat.S_IRWXG)
    except:
        print(
            "WARNING: It was not possible to change the permission to the following files: \n"
            + str(file_path))

def remove_dir(rm_dir):
    if not isinstance(rm_dir, pathlib.Path):
        rm_dir = pathlib.Path(rm_dir)

    if rm_dir.is_dir():
        print('removing:', rm_dir)
        shutil.rmtree(str(rm_dir))

def copy_file(input_path, output_path):
    ensure_dir_permissions(path=output_path.parent)
    shutil.copy(str(input_path), str(output_path))
    change_file_permissions(output_path)

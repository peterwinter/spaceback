#!/usr/bin/env python
__author__ = 'Peter B. Winter'
__email__ = 'peterwinteriii@gmail.com'
__status__ = 'prototype'

# standard imports
import os
import pathlib
import click
import shutil
import stat
import datetime


# Todo: make config file for globals
HOME = pathlib.Path('/Users/peterwinter')
DEFAULT_NAME = pathlib.Path('.spaceback')

SPACEMACS_DOT = pathlib.Path('.spacemacs')
EMACS_CONFIG = pathlib.Path('.emacs.d')
PATH = HOME / DEFAULT_NAME

class SpaceParts(object):

    def __init__(self, partname):
        self.part = partname
        self.home = pathlib.Path(home)
        self.spacedir = pathlib.Path(PATH)
        self.arcive_path = self. home /
        self.active_path =


class SpaceDot(SpaceParts):

class EmacsConfig(SpaceParts):


@click.group()
def main():
    # if ~/.spaceback does not exist make it
    if not PATH.is_dir():
        PATH.mkdir()


@click.command()
def archive():
    print('archive')

    if not SPACEMACS_DOT.is_file():
        print('dot spacemacs does not exist')
        return

    if not EMACS_CONFIG.is_dir():
        print('.emacs.d does not exist')
        return

    now = current_timestamp()
    backup_dir = PATH / '{now}'.format(now=now)

    copy_file(SPACEMACS_DOT, backup_dir)
    copy_dir(EMACS_CONFIG, backup_dir)
    print('done!')


@click.command()
def show():
    print('show')


@click.command()
def load():
    print('load')


main.add_command(archive)
main.add_command(show)
main.add_command(load)

###### permissions #####

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

def copy_file(input_path, output_path):
    ensure_dir_permissions(path=output_path.parent)
    shutil.copy(str(input_path), str(output_path))
    change_file_permissions(output_path)


def copy_dir(input_path, output_path):
    ensure_dir_permissions(path=output_path.parent)
    shutil.copytree(str(input_path), str(output_path))


def current_timestamp():
    today = datetime.datetime.today()
    current_timestamp = round(today.timestamp())
    return current_timestamp

def interpret_timestamp(ts):
    now = datetime.datetime.fromtimestamp(ts)
    return '{s}'.format(s=now)




if __name__ == '__main__':
    main()

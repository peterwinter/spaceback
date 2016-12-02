#!/usr/bin/env python
__author__ = 'Peter B. Winter'
__email__ = 'peterwinteriii@gmail.com'
__status__ = 'prototype'

# standard imports
import click
import pathlib
import os

# local imports
import sb

# Todo: make config file for globals
DEFAULT_NAME = pathlib.Path('.spaceback')
SPACEMACS_DOT = pathlib.Path('.spacemacs')
EMACS_CONFIG = pathlib.Path('.emacs.d')

HOME = pathlib.Path(os.getenv("HOME"))
PATH = HOME / DEFAULT_NAME

@click.group()
def main():
    # if ~/.spaceback does not exist make it
    if not PATH.is_dir():
        PATH.mkdir()

@click.command()
def archive():

    active_sm = sb.active_spacemacs()
    active_emc = sb.active_emacsconfig()

    backup_id = sb.current_id()
    print('archive --> {bid}'.format(bid=backup_id))
    backup_dir = PATH / '{now}'.format(now=backup_id)
    sb.ensure_dir_exists(backup_dir)
    # print(backup_id)
    # print(backup_dir, backup_dir.exists(), backup_dir.is_dir())

    bu_sm = sb.archived_spacemacs(backup_id)
    bu_em = sb.archived_emacsconfig(backup_id)
    # print(bu_sm)
    # print(bu_em)

    print('copying...', end=' ')
    sb.copy_file(active_sm, bu_sm)
    sb.copy_dir(active_emc, bu_em)
    print('done!')


# TODO: get it working
@click.command()
def show():
    print('show')


# TODO: get it working
@click.command()
def load():
    print('load')


main.add_command(archive)
main.add_command(show)
main.add_command(load)

if __name__ == '__main__':
    main()

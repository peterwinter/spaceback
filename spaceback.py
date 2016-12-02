#!/usr/bin/env python

# standard imports
import click

# local imports
import sb

__author__ = 'Peter B. Winter'
__email__ = 'peterwinteriii@gmail.com'
__status__ = 'prototype'

@click.group()
def main():
    """primary command line function, called with options"""
    # if ~/.spaceback does not exist make it
    sb.create_spacedir()

@click.command()
def archive():
    """saves active spacemacs configuration as new archive entry"""
    active_sm = sb.active_spacemacs()
    active_emc = sb.active_emacsconfig()

    backup_id = sb.current_id()
    print('archive --> {bid}'.format(bid=backup_id))

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
# @click.argument('backup_id', optional=True)
def show(): #backup_id):
    print('backups:')
    sb.show()


# TODO: get it working
@click.command()
@click.argument('backup_id')
def load(backup_id):
    print('loading backup: {bid}'.format(bid=backup_id))
    sb.run_load(backup_id)


main.add_command(archive)
main.add_command(show)
main.add_command(load)

if __name__ == '__main__':
    main()

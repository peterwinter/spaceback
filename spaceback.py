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
    """First paragraph.

    This is a very long second paragraph and as you
    can see wrapped very early in the source text
    but will be rewrapped to the terminal width in
    the final output.

    \b
    This is
    a paragraph
    without rewrapping.

    And this is a paragraph
    that will be rewrapped again.
    """
    # if ~/.spaceback does not exist make it
    sb.create_spacedir()

@click.command()
def save():
    """saves active spacemacs configuration"""
    active_sm = sb.active_spacemacs()
    active_emc = sb.active_emacsconfig()

    backup_id = sb.current_id()
    print('saving --> {bid}'.format(bid=backup_id))

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
    """shows all available backups"""
    print('backups:')
    sb.show()


# TODO: get it working
@click.command()
@click.argument('backup_id', nargs=-1)
def load(backup_id):
    """activates a backup"""
    print('loading backup: {bid}'.format(bid=backup_id))
    sb.run_load(backup_id)


main.add_command(save)
main.add_command(show)
main.add_command(load)

if __name__ == '__main__':
    main()

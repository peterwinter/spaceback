import os
import pathlib
import datetime

# Todo: make config file for globals
DEFAULT_NAME = pathlib.Path('.spaceback')
SPACEMACS_DOT = pathlib.Path('.spacemacs')
EMACS_CONFIG = pathlib.Path('.emacs.d')

HOME = pathlib.Path(os.getenv("HOME"))
PATH = HOME / DEFAULT_NAME

##############

def create_spacedir():
    if not PATH.is_dir():
        PATH.mkdir()


def active_spacemacs():
    return HOME / SPACEMACS_DOT


def active_emacsconfig():
    return HOME / EMACS_CONFIG


def backup_dir(sb_id):
    sb_id = '{sid}'.format(sid=sb_id)
    return PATH / sb_id


def remove_dot(filename):
    return '{}'.format(filename).strip('.')


def archived_spacemacs(sb_id):
    space_file = remove_dot(SPACEMACS_DOT)
    return backup_dir(sb_id) / space_file


def archived_emacsconfig(sb_id):
    emacs_dir = remove_dot(EMACS_CONFIG)
    return backup_dir(sb_id) / emacs_dir

##############


def current_id():
    today = datetime.datetime.today()
    current_timestamp = round(today.timestamp())
    return current_timestamp


def interpret_id(ts):
    date = datetime.datetime.fromtimestamp(ts)
    return '{d}'.format(d=date)


def active_exists():
    spacemacs_dot = active_spacemacs()
    emacs_config = active_emacsconfig()
    if not spacemacs_dot.is_file():
        print('dot spacemacs does not exist')
        return False
    if not emacs_config.is_dir():
        print('.emacs.d does not exist')
        return False
    return True

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

# TODO: break into small parts
def show():
    for backup_dir in PATH.glob('*'):
        backup_id = backup_dir.name
        bu_sm = archived_spacemacs(backup_id)
        bu_em = archived_emacsconfig(backup_id)
        # backup must be a directory
        if not backup_dir.is_dir():
            continue
        # backup must contain spacemacs file
        if not bu_sm.is_file():
            continue
        # backup must contain emacs.d dir
        if not bu_em.is_dir():
            continue
        # backup_id must be formated as timestamp
        try:
            time = int(backup_id)
        except ValueError:
            continue

        date = interpret_id(time)
        print(backup_id, '--', date)

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

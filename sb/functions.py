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

def active_spacemacs():
    return HOME / SPACEMACS_DOT

def active_emacsconfig():
    return HOME / EMACS_CONFIG

def archived_spacemacs(sb_id):
    sb_id = '{sid}'.format(sid=sb_id)
    return PATH / sb_id / '{}'.format(SPACEMACS_DOT).strip('.')

def archived_emacsconfig(sb_id):
    sb_id = '{sid}'.format(sid=sb_id)
    return PATH / sb_id / '{}'.format(EMACS_CONFIG).strip('.')

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

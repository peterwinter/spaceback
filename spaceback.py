#!/usr/bin/env python
"""spaceback

Usage:
  spaceback archive
  spaceback list
  spaceback activate <backup>
  spaceback (-h | --help)
  spaceback --version

Arguments:
  list
  activate
  <backup>

Options:
  -h  --help               Show this screen.
  --version                Show version.
"""

__author__ = 'Peter B. Winter'
__email__ = 'peterwinteriii@gmail.com'
__status__ = 'prototype'

# standard imports
import os
import pathlib
from docopt import docopt


def main():
    pass

if __name__ == '__main__':
    args = docopt(__doc__, version='spaceback 0.1')
    print(args)

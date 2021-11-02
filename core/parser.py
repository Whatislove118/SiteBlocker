import re
import sys

from .exceptions import ParseException
from .file_worker import add_site_to_block, delete_site_from_block, list_blocked_sites

commands = [
    ['block', add_site_to_block],
    ['unblock', delete_site_from_block],
    ['list', list_blocked_sites],
    ['exit', sys.exit]
]


# TODO валидация введенных данных
'''
input data: block www.facebook.com

\w+\s[[w]{3}]*

'''
def parse_command(command=None, command_pattern=None):
    if command_pattern is None:
        #command_pattern = r'\w+\s(([w]{3}\.[A-Za-z]+\.[A-Za-z]+\s*)+)+'
        command_pattern = r'\w+\s*(([w]{3}\.[A-Za-z]+\.[A-Za-z]+\s*)*)*'
    if command is None:
        raise ValueError('command shouldn\'t be None')

    _validate_command(command, command_pattern)
    command_type, command_args = _parse_command(command)

    for i, c in enumerate(commands):
        if command_type == c[0]:
            return c[1], command_args
    raise ParseException('Wrong command %s ' % command_type)


def _validate_command(command, pattern):
    # pattern = r'\w+\s(([w]{3}\.[A-Za-z]+\.[A-Za-z]+\s*)+)+'
    result = re.match(pattern, command)
    if result is None:
        raise ParseException('Parsing error: wrong command signature')

def _parse_command(command):
    pattern = r'\s'
    result = re.split(pattern, command)
    return result[0], result[1:]



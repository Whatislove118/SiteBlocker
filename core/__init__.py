import ctypes
import os
import sys
from sys import platform as _platform

DEBUG = False

WEBSITE_LIST = []

if DEBUG:
    HOST_FILE = 'hosts'
    REDIRECT_URL = '127.0.0.1'
    IS_ADMIN = (os.getuid() == 0)
else:
# TODO разобраться с различиями в макос и линукс
    if os.name == 'posix':
        HOST_FILE = '/etc/hosts'
        IS_ADMIN = (os.getuid() == 0)
    else:
        HOST_FILE = 'C:\Windows\System32\drivers\etc\hosts'
        IS_ADMIN = ctypes.windll.shell32.IsUserAnAdmin() != 0
    REDIRECT_URL = '127.0.0.1'

if not IS_ADMIN:
    print('This program requires administrator privileges. Please, run program as administrator.')
    print('Press any key to close the program')
    input()
    sys.exit(1)

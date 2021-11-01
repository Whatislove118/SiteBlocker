import os
from sys import platform as _platform

DEBUG = False

WEBSITE_LIST = []

if DEBUG:
    HOST_FILE = 'hosts'
    REDIRECT_URL = '127.0.0.1'
else:
# TODO разобраться с различиями в макос и линукс
    if os.name == 'posix':
        HOST_FILE = '/etc/hosts'
    REDIRECT_URL = '127.0.0.1'

print(os.name)
print(_platform)

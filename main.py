from core import *
from core.file_worker import add_site_to_block, delete_site_from_block
from core.parser import parse_command

greeting_message = 'Commands:\n 1. block [ips separate by ,]\n 2. unblock [ips separate by ,]'

def main():
    print(greeting_message)
    while True:
        print('command...')
        command = input()
        command, site = parse_command(command)
        if command == 'block':
            add_site_to_block(HOST_FILE, site, REDIRECT_URL)
        if command == 'unblock':
            delete_site_from_block(HOST_FILE, site, REDIRECT_URL)


file = open(HOST_FILE, 'r')
for l in file:
    print(l)


if __name__ == '__main__':
    main()


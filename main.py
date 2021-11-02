from core import *

from core.exceptions import ParseException

from core.parser import parse_command

greeting_message = 'Commands:\n 1. block [site1 site2 ...]\n 2. unblock [site1 site2 ...]\n 3. list'

def main():
    print(greeting_message)
    while True:
        print('command...')
        command = input()
        try:
            action, sites = parse_command(command)
            action(HOST_FILE, sites, REDIRECT_URL)
            print('Done')
        except ParseException as e:
            print('Exception: %s' % e.message)


if __name__ == '__main__':
    main()



commands = [
    ['block', []],
    ['unblock', []],
]


# TODO валидация введенных данных
def parse_command(command=None):
    if command is None:
        raise ValueError('command shouldn\'t be None')
    command_type, command_args = command.split(' ')
    for i, c in enumerate(commands):
        if command_type == c[0]:
            return c[0], command_args






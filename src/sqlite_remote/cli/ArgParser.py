from sys import argv


def get_option(name: str, args=argv[1:], default_value=None) -> str:
    i = 0
    for arg in args:
        if arg == name:
            if len(args) - 1 > i:
                return args[i + 1]
            break
        i += 1
    return default_value


def get_flag(name: str, args=argv[1:]) -> bool:
    """Determines whether or not a flag is present"""
    return name in args


def get_positional(position: int, possible_flags: list, args=argv[1:]):
    """Gets a particular positional argument (by position)"""
    if position < 0:
        raise Exception("Position is less than 0")
    i = 0
    while i < len(args):
        arg = str(args[i])
        if arg == "":
            raise Exception("Arg is empty")
        if arg in possible_flags:
            continue
        if arg.startswith('-'):
            i += 2
        if position == 0:
            return arg
        position -= 1
    return None


def get_positionals(possible_flags: list, args=argv[1:]) -> list:
    """Gets all positional arguments"""
    positionals = []
    i = 0
    while i < len(args):
        arg = str(args[i])
        if arg == "":
            raise Exception("Arg is empty")
        if arg in possible_flags:
            continue
        if arg.startswith('-'):
            i += 2
        positionals.append(arg)
    return positionals


def map_arguments(flags=[], positional_keys=[], args=argv[1:]) -> dict:
    rv = {}
    i = 0
    n_positionals = 0
    while i < len(args):
        arg = str(args[i])
        if arg == "":
            raise Exception("Arg is empty")
        if arg in flags:
            rv[arg] = True
            flags.remove(arg)
            i += 1
        elif arg.startswith('-'):
            if i == len(args) - 1:
                raise Exception("Option not followed by value")
            if arg in positional_keys:
                positional_keys.remove(arg)
            rv[arg] = args[i + 1]
            i += 2
        elif n_positionals == len(positional_keys):
            raise Exception(f"Unexpected argument '{arg}'")
        else:
            rv[positional_keys[n_positionals]] = arg

    for f in flags:
        rv[f] = False
    return rv

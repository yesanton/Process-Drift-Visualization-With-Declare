from src.auxiliary.constant_definitions import NAME_FILE_SEPARATOR

def compose_name(*argv):
    name = ''
    # correctly identify the extension of the file
    end = len(argv) - 1
    if argv[-1][0] == '.':
        end -= 1

    for arg in argv[:end]:
        name +=  str(arg) + NAME_FILE_SEPARATOR

    for arg in argv[end:]:
        name += str(arg)

    return name
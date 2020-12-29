def __print_margins(title_length):
    print('--', end = '')
    for x in range(title_length):
        print('-', end = '')
    print('--', end = '')
    print()

def print_title(title):
    __print_margins(len(title))
    print('| ' + title + ' |')
    __print_margins(len(title))
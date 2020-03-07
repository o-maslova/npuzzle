import sys


def parse_board_lines(field_lst: list, field_size: int):
    field = []
    for string in field_lst:
        comment_indx = string.find('#')
        string = string if comment_indx == -1 else string[:comment_indx]
        tmp_lst = [elem for elem in string.split(" ") if elem != '']
        # print(tmp_lst)
        if len(tmp_lst) != field_size:
            sys.exit("Wrong number of elements in string!")
        try:
            field.append([int(digit) for digit in tmp_lst])
        except Exception as err:
            sys.exit(err)
    if len(field) != field_size:
        sys.exit("Wrong number of strings!")
    return field


def create_board(data: list):

    field_size = 0
    for elem in data:
        if elem[0] is '#':
            continue
        elif elem.isdigit() is False:
            # print(elem, len(elem))
            sys.exit("No determined size of the board!")
        else:
            field_size = int(elem)
            next_value = data.index(elem) + 1
            if next_value < len(data):
                return parse_board_lines(data[next_value:], field_size)
            else:
                sys.exit("Wrong file format 1!")


def parsing(string: str):
    # Check if this file exist
    try:
        file_text = [line.rstrip('\n') for line in open(string, 'r')]
        # with open(string, 'r') as fd:
        #     file_text = []
        #     line = fd.readline()
        #     while line:
        #         file_text.append(line)
        #         line = fd.readline()
        return create_board(file_text)
    except IOError as err:
        print(err)


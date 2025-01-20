
# input_list - a string containing a list of elements each separated by a newline
# col_size - the max number of elements in a column
def format_list(input_list, col_size):

    if col_size < 1:
        col_size = 1

    arr = input_list.splitlines()

    # Finds the longest element in mylist
    maxWidth = max(map(lambda x: len(x), arr))

    # Sets all elements of mylist to size maxWidth with left align
    justifyList = list(map(lambda x: x.ljust(maxWidth), arr))

    size = len(input_list.splitlines())

    if size % col_size == 0:
        num_col = size // col_size
    else:
        if size < col_size:
            num_col = 1
        else:
            num_col = size // col_size + 1

        empty_space = col_size - size % col_size
        for i in range(empty_space):
            justifyList.append('')

    return '\n'.join(' '.join(justifyList[r + c * col_size] for c in range(num_col)) for r in range(col_size))

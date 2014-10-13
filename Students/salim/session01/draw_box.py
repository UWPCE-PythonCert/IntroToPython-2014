def print_grid(size, boxes):

    # adjust wrong inputs
    size, boxes = adjust_inputs(size, boxes)

    # rows of grid
    row_count = 0
    for i in range(size):

        # if row is a solid line
        if row_count % (size / boxes) == 0:

            print_row(width=size, row_type='solid', boxes=boxes)

        # if row is a non-solid line
        else:

            print_row(width=size, row_type='non-solid', boxes=boxes)

        # increment row_count
        row_count += 1


def print_row(width, row_type, boxes):

    # set row type
    if row_type == 'solid':
        outside = '+'
        inside = '-'
    elif row_type == 'non-solid':
        outside = '|'
        inside = ' '

    # columns of row
    col_count = 0
    for ii in range(width):

        # if middle of row
        if col_count < (width - 1):

            if col_count % (width / boxes) == 0:
                print outside,   # include commas to keep text on same line
            else:
                print inside,   # include commas to keep text on same line

        # if end of row
        else:

            if col_count % (width / boxes) == 0 or boxes == 1:
                print outside
            else:
                print inside

        # increment col_count
        col_count += 1


def adjust_inputs(size, boxes):

    # if size input is even, change to next biggest odd number
    if size % 2 == 0:
        size_result = size + 1
    else:
        size_result = size

    # min of boxes value 1 and boxes value not greater than size_result
    if boxes <= 1:
        boxes_result = 1
    elif boxes > size_result:
        boxes_result = size_result
    else:
        boxes_result = boxes

    return size_result, boxes_result

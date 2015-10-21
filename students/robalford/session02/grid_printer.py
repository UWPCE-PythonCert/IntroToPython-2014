def print_grid(size, rows_and_columns):
    # return value, then print function
    plus_row = ('+ ' + '- ' * size) * rows_and_columns + '+ \n'
    pipe_row = ('| ' + '  ' * size) * rows_and_columns + '| \n'
    grid = (plus_row + pipe_row * size) * rows_and_columns + plus_row
    return grid
    

    
    
    
    
    
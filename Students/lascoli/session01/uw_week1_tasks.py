def grid_maker(units):
    
    border = '+ ' + ' - ' *((units -3)/2) + ' + ' + ' - ' *((units -3)/2) + ' + ' + '\n'
    middle = '| ' + '   ' *((units -3)/2 )+ ' | ' + '   ' *((units -3)/2) + ' + ' + '\n'
    grid = border + middle *((units -3)/2)
    
    print grid * 2 + border
      

grid_maker(5)

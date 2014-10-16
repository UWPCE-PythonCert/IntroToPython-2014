def grid_maker(units):
    units = 11
    
##define border_line
    border = '+ ' + ' - ' *((units -3)/2) + ' + ' + ' - ' *((units -3)/2) + ' + '
                    
##define mid_line
    middle = '| ' + '   ' *((units -3)/2 )+ ' | ' + '   ' *((units -3)/2) + ' + '

    print border
    print middle * ((units -3)/2)
    print border
    print middle * ((units -3)/2)
    print border
    
grid_maker(11)
     
     
         
    
    
    


 
  


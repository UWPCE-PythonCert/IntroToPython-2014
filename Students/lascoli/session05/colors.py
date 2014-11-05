colors =("black","red")
colors2 = dict(link_color ="yellow",visited_link_color="green")

def color_fun(*argv,**kwargs):
    
    print "\nThe fore_color is",argv[0],"\n"
    print "The back_color is",argv[1],"\n"
    print "The link_color is", kwargs["link_color"],"\n"
    print "The visited_link_color is",kwargs["visited_link_color"],"\n"
    
 
color_fun(*colors,**colors2) 
def color_fun(*args, **kwargs):
   print ('The foreground color is:',args[0])
   print ('The background  color is:',args[1])
   print ('The link color is:', kwargs)
   print ('The visited link color is:', kwargs)
color_fun('black', 'red', link_color='blue', visited_link_color='yellow')
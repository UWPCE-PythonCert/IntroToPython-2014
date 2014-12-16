def front_back(str):
   if len(str) == 1:
       return(str)
   else:
       front = str[:1]
       back = str[len(str)-1:]
       middle = str[1:(len(str)-1)]
       newstr =  back + middle + front
       return newstr


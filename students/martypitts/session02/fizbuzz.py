result = 1

# end print_grid1

# multiple of 3
def mult3check(numin):
      if (numin % 3 == 0):
         return True
      else:
         return False
      # end if
# end print_grid1

# multiple of 5
def mult5check(numin):
      if (numin % 5 == 0):
         return True
      else:
         return False
      # end if
# end print_grid1

# for numbers from 0 - 100 check print fizz for numbers divisable by 3 and buzz for numbers divisible by 5
for numgen in range(0, 100): 
   resultdiv3 = mult3check(int(numgen))
   resultdiv5 = mult5check(int(numgen))
   if resultdiv3 == False and resultdiv5 == False:
      print(numgen)
   elif resultdiv3 == True and resultdiv5 == False:
      print("Fizz")
   elif resultdiv3 == False and resultdiv5 == True:
      print("Buzz")
   elif resultdiv3 == True and resultdiv5 == True:
      print("FizzBuzz")
# End if  



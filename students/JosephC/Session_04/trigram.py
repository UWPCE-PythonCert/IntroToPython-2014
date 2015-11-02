#Trigam
#From http://codekata.com/kata/kata14-tom-swift-under-the-milkwood/
"""
A text file, sherlock.txt, is read from and its contents are rearranged to create new sentences
Words are set as key/value pairs, and then the newly constructed sentences are created from these key/values
"""
#import random to allow me to pull a random number line fron the Sherlock text
import random 


a = {'I may': 'I', 'may I': 'wish', 'I wish': ('I', 'I'), 'wish I': ('may', 'might')}

for i in a:
    print("the {}th item is {}".format(i, a))

#random.choice()

#create variables to hold each line read from sherlock and then to hold the random choice of line
#line = f.readline('sherlock.txt')
#randomline = random.choice(line)  

#run through sherlock; the loop exits when there are no more lines
#else if there are lines, then a statement is formatted so that an original line is printed along with a random line right after it
#THE THING IS: I need random words, not sentences, hooked up with words to create new sentences
#while True:
 #   if not line:
  #      break
   # else:
#        print("{}{}".format(line, randomline))


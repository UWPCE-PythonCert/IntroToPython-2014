Coding Bat examples
######################

Warmup-1 > monkey_trouble 
============================

We have two monkeys, a and b, and the parameters a_smile and b_smile indicate if each is smiling. We are in trouble if they are both smiling or if neither of them is smiling. Return True if we are in trouble::

  monkey_trouble(True, True) → True
  monkey_trouble(False, False) → True
  monkey_trouble(True, False) → False


Warmup-1 > sleep_in 
=======================

The parameter weekday is True if it is a weekday, and the parameter vacation is True if we are on vacation. We sleep in if it is not a weekday or we're on vacation. Return True if we sleep in. 

sleep_in(False, False) → True
sleep_in(True, False) → False
sleep_in(False, True) → True


Warmup-1 > diff21 
=======================

Given an int n, return the absolute difference between n and 21, except return double the absolute difference if n is over 21. 

diff21(19) → 2
diff21(10) → 11
diff21(21) → 0

Warmup-1 > makes10 
======================

Given 2 ints, a and b, return True if one if them is 10 or if their sum is 10. 

makes10(9, 10) → True
makes10(9, 9) → False
makes10(1, 9) → True

Logic-1 > cigar_party 
======================

When squirrels get together for a party, they like to have cigars. A squirrel party is successful when the number of cigars is between 40 and 60, inclusive. Unless it is the weekend, in which case there is no upper bound on the number of cigars. Return True if the party with the given values is successful, or False otherwise. 

cigar_party(30, False) → False
cigar_party(50, False) → True
cigar_party(70, True) → True


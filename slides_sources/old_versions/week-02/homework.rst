Homework: week 2 (due week 3)
##############################

Adapted from "Think Python": Chapter 6, excercise 5.


The Ackermann function, A(m, n), is defined::

  A(m, n) =   
              n+1   if  m = 0 
        A(m−1, 1)   if  m > 0  and  n = 0 
  A(m−1, A(m, n−1))   if  m > 0  and  n > 0.


See http://en.wikipedia.org/wiki/Ackermann_function.

Write a function named ack that evaluates Ackermann’s function.
Use your function to evaluate ack(3, 4), which should be 125.

What happens for larger values of m and n? 
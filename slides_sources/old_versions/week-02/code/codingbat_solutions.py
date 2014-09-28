#!/usr/bin/env python

"""
Coding Bat Example Solutions
"""

##############################
## Warmup-1 > monkey_trouble 

def monkey_trouble(a_smile, b_smile):
	"""
	really simple solution
	"""
    if a_smile and b_smile:
        return True
    elif not a_smile and not b_smile:
        return True
    else:
        return False

def monkey_trouble2(a_smile, b_smile):
	"""
	slightly more sophisticated
	"""
    if a_smile and b_smile or not (a_smile or b_smile):
        return True
    else:
        return False

def monkey_trouble3(a_smile, b_smile):
	"""
	conditional expression -- kind of ugly in this case
	"""
    result = True if (a_smile and b_smile or not (a_smile or b_smile)) else False
    return result

def monkey_trouble4(a_smile, b_smile):
	"""
	direct return of boolean result
	"""
    return a_smile and b_smile or not (a_smile or b_smile)

##############################
## Warmup-1 > sleep_in 

def sleep_in(weekday, vacation):
	"""
	basic solution
	"""
    if (not weekday) or vacation:
        return True
    else:
        return False  

def sleep_in2(weekday, vacation):
	"""
	direct return of boolean result
	"""
    return (not weekday) or vacation

##################
## Warmup-1 > diff21

def diff21(n):
	"""
	basic solution
	"""
    if n > 21:
        return 2 * (n - 21)
    else:
        return 21 - n

def diff21b(n):
	"""
	direct return of conditional expression
	"""
    return 2 * (n - 21) if n > 21 else 21-n


###############
## Warmup-1 > makes10 

def makes10(a, b):
	"""
	Too easy to make a one-liner
	"""
    return a == 10 or b == 10 or a+b == 10

######################
## Logic-1 > cigar_party 

def cigar_party(cigars, is_weekend):
	"""
	basic solution
	"""
    if is_weekend and cigars >= 40:
            return True
    elif 40 <= cigars <= 60:
        return True
    return False  

def cigar_party2(cigars, is_weekend):
    """
    some direct return of bool result
    """
  	if is_weekend:
    	return (cigars >= 40)
  	else:
    	return (cigars >= 40 and cigars <= 60)

def cigar_party3(cigars, is_weekend):
    """
    conditional expression
    """
    return (cigars >= 40) if is_weekend else (cigars >= 40 and cigars <= 60)

#!/usr/bin/env python

# EXCEPTIONS LAB: Improving 'raw_input'

# The raw_input() function can generate two exceptions: 
# EOFError or KeyboardInterrupt on end-of-file(EOF) or canceled input.

# Create a wrapper function, perhaps safe_input() that returns None 
# rather than raising these exceptions, when the user enters 
# ^C for Keyboard Interrupt, or 
# ^D (^Z on Windows) for End Of File

def safe_input(prompt='Enter input: '):
	try:
		raw = raw_input(prompt)
		return raw
	except (KeyboardInterrupt, EOFError) as the_error:
		return None
		# raise

# Update your mailroom program to use exceptions (and IBAFP) to handle malformed numeric input
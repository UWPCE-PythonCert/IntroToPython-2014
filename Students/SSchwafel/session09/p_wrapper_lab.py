#!/usr/bin/python

def p_wrapper_func(func, tag):
    
    def tagger(tag):

        tag_type = raw_input("Tag? ")
        tag_type = tag_type.title()

        return tag_type

    def p_wrapper(*args, **kwargs):
        tag_type = tag
        user_input = func(*args, **kwargs)
        #return "<p> {} </p>".format(user_input)
        return "<{}> {} </{}>".format(tag, user_input, tag)
    return p_wrapper

@p_wrapper_func
def print_test_string():
    test_text = "this is a test string"
    return test_text

print print_test_string()

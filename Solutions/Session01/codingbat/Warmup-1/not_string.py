#!/usr/bin/env python


def not_string(st):
    if st.startswith('not'):
        return st
    else:
        return 'not ' + st


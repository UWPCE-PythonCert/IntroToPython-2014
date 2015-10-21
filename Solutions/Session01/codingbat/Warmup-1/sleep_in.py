#!/usr/bin/env python


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

#!/usr/bin/python3

def safe_print_integer(value):
    try:
        print("{:d}".format(value))
    except(ValueError, TypeError):
        return False
    finally:
        if not succeeded:
            return False
        else:
            return True

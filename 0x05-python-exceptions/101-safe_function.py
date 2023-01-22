#!/usr/bin/python3
def safe_function(fct, *args):
    # func-function to execute
    # args-arguments for fct
    # Execute the function safely
    try:
        exc_func = fct(*args)
        return exc_func
    except (TypeError IndexError ZeroDivisionError):
        print("Exception: {}".format(sys.exc_info()[1]), file=sys.stderr)
        return (None)

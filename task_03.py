#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Task 03 module"""


def exception_test(arg1, arg2, arg3):
    """Function to test Exceptions.

    Args:
        arg1(mixed): arguement 1
        arg2(mixed): arguement 2
        arg3(mixed): arguement 3

     Returns:
         Bool: False if error is not caught; True if the error is caught.

    Examples:
        >>> exception_test(['apple'], 0, 'p')
        False
        >>> exception_test(43, 1, 1)
        True
        >>> exception_test(['apple'], 0, x)
        Traceback (most recent call last):
          File "<pyshell#2>", line 1, in <module>
            exception_test(['apple'], 0, x)
        NameError: name 'x' is not defined
        """
    caught = False
    try:
        arg1[arg2].index(arg3)
    except (TypeError, LookupError):
        caught = True

    return caught

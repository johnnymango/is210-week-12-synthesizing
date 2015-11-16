#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Task 02 error classes."""


class CustomError(Exception):
    """Custom Error Class.

    Atributes:
        None
    """

    def __init__(self, errormsg, cause):
        """Constructor for CustomError class.

        Args:
            errormsg(str):  The custom error message.
            cause(str): The custom cause message.

        Attributes:
            Exception(class): initializes Exception constructor.
            errormsg(str):  The custom error message.
            cause(str): The custom cause message.
        """
        Exception.__init__(self)
        self.errormsg = errormsg
        self.cause = cause

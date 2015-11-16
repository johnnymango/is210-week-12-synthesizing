#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Error Classes"""


class BaseError(Exception):
    """BaseError class"""
    pass


class StringError(BaseError, TypeError):
    """StringError class"""
    pass


class NumberError(BaseError, TypeError):
    """NumberError class"""
    pass


class NonZeroError(NumberError):
    """NonZeroError class"""
    pass

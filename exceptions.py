"""Exceptions"""

class InvalidArgumentException(Exception):
    """User provides the wrong type for an argument"""
    def __init__(self, message):
        self.message = message

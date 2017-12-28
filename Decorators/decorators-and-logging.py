#!/usr/bin/python
""" A simple example of how to use logging module with any function to measure the time of execution """

import logging
from time import time
from random import randint

# create a logger
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

# create a file handler
handler = logging.FileHandler('history.log')
handler.setLevel(logging.INFO)

# create a formatter for your log file
formatter = logging.Formatter('%(asctime)s: %(message)s', "%Y-%m-%d %H:%M:%S")
handler.setFormatter(formatter)

# combine handler and logger
logger.addHandler(handler)


def logging_decorator(f):
    """ This decorator will take a function as an argument and log its args and exec time (history.log)."""

    def wrap(*args, **kwargs):
        t = time()
        func = f(*args, **kwargs)
        logger.info('\nFunction: {}'
                    '\nArgs: {}'
                    '\nExecution time: {}'
                    '\n'.format(f.__name__, args, time() - t))

        return func
    return wrap

@logging_decorator
def my_superb_function(a=0, b=0):
    """ A simple function to add two numbers together """
    return ('{} + {} = {}'.format(a, b, a + b))

# create random numbers
a = randint(1,100)
b = randint(1,100)

# Print and log the result
print(my_superb_function(a,b))

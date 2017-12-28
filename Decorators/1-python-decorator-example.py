#!/usr/bin/python
""" A very simple example of how to use decorators to add additional functionality to your functions. """


def greeting_message_decorator(f):
    """ This decorator will take a func with all its contents and wrap it around WRAP func.
    This will create additional functionality to the 'greeting_message' func by printing messages."""

    def wrap(*args, **kwargs):
        """ Here we can print *aregs and **kwargs and manipulate them """

        print('>> Decorate before executing "greeting_message" function')
        func = f(*args, **kwargs)
        print('>> Decorate after executing "greeting_message" function')
        return func
    return wrap

@greeting_message_decorator
def greeting_message(name):
    """ This function will be decorated by 'greeting_message_decorator' before execution """
    print('My name is ' + name)

greeting_message('Adam')
import logging
import random

logging.basicConfig(filename='test.log',
                    filemode='a',
                    format='%(asctime)s %(levelname)s-%(message)s',
                    datefmt='%Y-%d %H:%M:%S')
for i in  range(0,15):
    if(i%2==0):
        logging.warning('Log Warning Message')
    elif(i%3==0):
        logging.critical('Log Critical Message')
    else:
        logging.error('Log Error Message')





def add(x, y):
    """Add Function"""
    return x + y

def subtract(x, y):
    """Subtract Function"""
    return x - y

def multiply(x, y):
    """Multiply Function"""
    return x * y


def divide(x, y):
    """Divide Function"""
    return x / y


num_1 = 10
num_2 = 5
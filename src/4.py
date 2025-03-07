import random

def get_random_number(n):
    return random.randint(1, n)

def get_random_string(n):
    return ''.join(random.choice('abcdefghijklmnopqrstuvwxyz') for i in range(n))

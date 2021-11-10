import random
import string

def generator():
    return ''.join(random.choices(string.ascii_lowercase + string.digits, k=6))
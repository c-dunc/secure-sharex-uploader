import random
import string

def generate_filename(length):
    letters = string.ascii_letters
    filename = ''.join(random.choices(letters, k=length))
    return filename

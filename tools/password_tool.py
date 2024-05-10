import random
import string
import hashlib

def generate_password(length):
    characters = string.ascii_letters + string.digits
    password = ''.join(random.choice(characters) for i in range(length))
    return password

def calculate_hash(text, algorithm):
    hash_obj = hashlib.new(algorithm)
    hash_obj.update(text.encode())
    return hash_obj.hexdigest()

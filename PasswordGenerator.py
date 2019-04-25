import string
import random

def generatePassword():
    passwordResult = "".join(random.sample(string.ascii_letters + string.digits + string.punctuation, random.randrange(4, 16)))
    print(passwordResult)

import string
import random
import time
import math
import os
import sys

class passgen:
    def generate_key(self,length):
        random.seed(random.random())
        keygen = lambda y:''.join([self.characters[int(random.random()*len(self.characters))] for i in range(0,int(y))])
        return keygen(length)

    def __init__(self):
        self.characters=string.ascii_letters+'0123456789'

    def check_modules(self):
        try:
            global Random
            import quantumrandom as Random
        except ImportError:
            if sys.version_info[0] > 3:
                os.system("pip3 install quantumrandom")
            else:
                os.system("pip install quantumrandom")
            global Random
            import quantumrandom as Random

    def secure_key(self,length):
        self.check_modules()
        keygen = lambda y:''.join([self.characters[int(Random.randint(0,len(self.characters)))] for i in range(0,int(y))])
        return keygen(length)

    def usage(self):
        print("Usage:\n\nTo generate pseudo-random key: passgen.generate_key(length)\nTo generate secure true-random key: passgen.secure_key(length)\n")
if __name__ == "__main__":
    p = passgen()
    p.usage()
    print(p.generate_key(66))
    print(p.secure_key(66))

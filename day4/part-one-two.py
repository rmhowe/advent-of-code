#
# Learned about strip(), very important! Now I'm confused as to whether I should
# use learned or learnt, dilemmas. Learnt about startswith(), and str() for
# printing ints.
#
# This is a pretty naive solution, might come back to it later
#

import sys
import hashlib

def get_key_part(secret_key_file):
    secret_key = secret_key_file.read().strip()
    key_part = 0
    digest = ''
    while not digest.startswith('000000'):
        key_part += 1
        digest = hashlib.md5(secret_key + str(key_part)).hexdigest()

    return key_part

if len(sys.argv) > 1:
    file_name = sys.argv[1]
else:
    file_name = 'input.txt'
secret_key_file = open(file_name, 'r')
print get_key_part(secret_key_file)
secret_key_file.close()

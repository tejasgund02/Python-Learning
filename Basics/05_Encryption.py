'''
# Encryption and Decryption
if you want to encrypt a message, you can use the following code:
    message = 'tejas'
    result = 'asdejastljf' --> this is the encrypted message first 3 char random and last 3 char random and in between this first char at last.
'''
import random
def encrypt(message):
    result = ''
    if len(message) < 3:
        return message[::-1]
    else:
        chars = list(message)
        first_char = chars[0]
        chars.pop(0)
        chars.append(first_char)
        result = ''.join(chars)
        random_chars = 'asdejastljfqwerqpiuo'
        prefix = ''.join(random.choices(random_chars, k=3))
        suffix = ''.join(random.choices(random_chars, k=3))
        # result = prefix + result + suffix
        # result = random.choice(random_chars, k=3) + result + random.choice(random_chars, k=3)
        return prefix + result + suffix

print(encrypt('tejas'))
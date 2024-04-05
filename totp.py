from hashlib import sha1
from time import time


def generateCode(key, T0=0, Tx=30):
    T = time()

    # HOTP
    Ct = round((T - T0) / Tx)
    CtK = key.encode() + Ct.to_bytes(8, "big")

    # Hashing the secret and Ct
    digest = sha1(CtK).hexdigest()

    # Extracting the OTP
    code = int(digest, 16) % (10**6)

    return code


a = generateCode("superSecretKey")
print(a)

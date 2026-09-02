# SQN = a2b("--")
# AMF = a2b(2--"")

#outputs

# IN1 = SQN+AMF+SQN+AMF

#output blir en hex/ascii som man kan konvertere selv

"""
Milenage Test Set 1
3GPP TS 35.207
"""

from a2b import a2b

# Subscriber key (128 bits)
K = a2b("465b5ce8 b199b49f aa5f0a2e e238a6bc")

# Random challenge (128 bits)
RAND = a2b("23553cbe 9637a89d 218ae64d ae47bf35")

# Sequence number (48 bits)
SQN = a2b("ff9bb4d0 b607")

# Authentication Management Field (16 bits)
AMF = a2b("b9b9")

# Operator Variant Algorithm Configuration Field (128 bits)
OP = a2b("cdc202d5 123e20f6 2b6d676a c72cb318")

# Utskrift for verifikasjon
if __name__ == "__main__":
    print("K    =", K.hex())
    print("RAND =", RAND.hex())
    print("SQN  =", SQN.hex())
    print("AMF  =", AMF.hex())
    print("OP   =", OP.hex())
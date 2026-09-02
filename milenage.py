from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
#fra a2b import a2b, rotating ...



def aes_encrypt(key: bytes, plaintext: bytes) -> bytes:

    cipher = Cipher(algorithms.AES(key), modes.ECB())

    encryptor = cipher.encryptor()

    return encryptor.update(plaintext) + encryptor.finalize()


#
def xor_bytes(a: bytes, b: bytes) -> bytes:
    return bytes(x ^ y for x, y in zip(a, b))



def rotate_left(data: bytes, n: int) -> bytes:

    return data[n:] + data[:n]


# Man trenger et random generert input (trengr man å legge til?) - denne er gitt
def f0(randomNumber):
    return

#rart at den ligger i en class?
class Milenage: 

    def __init__(self, k: bytes, opc: bytes):
        self.k = k
        self.opc = opc

# f1 = MAC = (SQN||AMF||RAND)
    def f1(self, rand, sqn, amf):
        pass

#f2 = XRES = rand
    def f2(self, rand):
        pass

# f3 = CK 
    def f3(self, rand):
        pass

# f4 = IK
    def f4(self, rand):
        pass

#f5 = AK
    def f5(self, rand):
        pass


# OPerator specific field (OP) er gitt fra "operatør" og brukes med en nøkkel for å verifisere abonnementet

# Five integers r1, r2, r3, r4, r5 are defined as follows: (rotation constants)

r1 = 64;
r2 = 0;
r3 = 32;
r4 = 64;
r5 = 96


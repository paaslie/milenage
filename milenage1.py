from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes

# Hjelpefunksjoner
# Hjelpefunksjoner ligger i en annen mappe FORETRUKKENT) Så encryption.py er overflødig nå.

def aes_encrypt(key: bytes, plaintext: bytes) -> bytes: # AES kryptering
    cipher = Cipher(algorithms.AES(key), modes.ECB())
    encryptor = cipher.encryptor()
    return encryptor.update(plaintext) + encryptor.finalize()


def xor_bytes(a: bytes, b: bytes) -> bytes: #XOR
    return bytes(x ^ y for x, y in zip(a, b))


def rotate_left(data: bytes, n: int) -> bytes: #Rotating
    return data[n:] + data[:n]


def compute_opc(k: bytes, op: bytes) -> bytes: #AES kryptering
    """
    OPc = AES(K, OP) XOR OP
    """
    return xor_bytes(aes_encrypt(k, op), op) #bruker xor_bytes med: K, OP


# Rotasjonskonstanter og c

r1 = 8      # 64 bit
r2 = 0      # 0 bit
r3 = 4      # 32 bit
r4 = 8      # 64 bit
r5 = 12     # 96 bit

c1 = bytes.fromhex("00000000000000000000000000000000")
c2 = bytes.fromhex("00000000000000000000000000000001")
c3 = bytes.fromhex("00000000000000000000000000000002")
c4 = bytes.fromhex("00000000000000000000000000000004")
c5 = bytes.fromhex("00000000000000000000000000000008")

# Milenage seksjonen
class Milenage:

#OPC
    def __init__(self, k: bytes, opc: bytes):
        self.k = k
        self.opc = opc

#AES krypteringen og XOR gjenbrukt
    def _temp(self, rand: bytes) -> bytes:
        return aes_encrypt(
            self.k,
            xor_bytes(rand, self.opc)
        )


    # f1 -> MAC-A

    def f1(self, rand: bytes, sqn: bytes, amf: bytes) -> bytes:

        temp = self._temp(rand)

        in1 = sqn + amf + sqn + amf

        rijndael_input = xor_bytes(
            rotate_left(
                xor_bytes(in1, self.opc),
                r1
            ),
            temp
        )

        out1 = aes_encrypt(self.k, rijndael_input)

        mac_a = xor_bytes(out1, self.opc)[:8]

        return mac_a

    # -------------------------------------------------
    # f2 -> RES
    # -------------------------------------------------

    def f2(self, rand: bytes) -> bytes:

        temp = self._temp(rand)

        out = xor_bytes(temp, self.opc)

        res = out[8:16]

        return res

    # -------------------------------------------------
    # f3 -> CK
    # -------------------------------------------------

    def f3(self, rand: bytes) -> bytes:

        temp = self._temp(rand)

        inp = xor_bytes(temp, self.opc)
        
        inp = rotate_left(inp, r3)
       
        inp = xor_bytes(inp, c3)
        
        out = aes_encrypt(self.k, inp)
        
        ck = xor_bytes(out, self.opc)

        return ck

    # -------------------------------------------------
    # f4 -> IK
    # -------------------------------------------------

    def f4(self, rand: bytes) -> bytes:

          temp = self._temp(rand)
          
          inp = xor_bytes(temp, self.opc)
        
          inp = rotate_left(inp, r4)

          inp = xor_bytes(inp, c4)
          
          out = aes_encrypt(self.k, inp)  
           
          ik = xor_bytes(out, self.opc)
                

          return ik

    # -------------------------------------------------
    # f5 -> AK
    # -------------------------------------------------

    def f5(self, rand: bytes) -> bytes:

        temp = self._temp(rand)

        inp = xor_bytes(temp, self.opc)

        inp = rotate_left(inp, r2)

        inp = xor_bytes(inp, c2)

        out = aes_encrypt(self.k, inp)

        ak = xor_bytes(out, self.opc)[:6]

        return ak

"""
MAngler 1* og 5* funksjoner
"""
        
# Test mot in1.py

# Per nå her ligger testdataene

if __name__ == "__main__":

    from in1 import K, RAND, SQN, AMF, OP

    opc = compute_opc(K, OP)

    print("K    =", K.hex())
    print("RAND =", RAND.hex())
    print("SQN  =", SQN.hex())
    print("AMF  =", AMF.hex())
    print("OP   =", OP.hex())
    print("OPc  =", opc.hex())

    m = Milenage(K, opc)

    print("\nf1 (MAC-A):", m.f1(RAND, SQN, AMF).hex())
    print("f2 (RES):  ", m.f2(RAND).hex())
    print("f3 (CK):   ", m.f3(RAND).hex())
    print("f4 (IK):   ", m.f4(RAND).hex())
    print("f5 (AK):   ", m.f5(RAND).hex())

    print("r5 =", r5)
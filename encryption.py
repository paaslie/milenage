# en funksjon som krypterer Ek()

from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
def E(k, m: bytes) -> bytes:
    #AES128 in ECB mode
    assert len(m) == 16, "E(k,m): Input block m must be 16 bytes long (was {:d}).".format(len(m))
    assert len(k) == 16, "E(k,m): key must be 16 bytes long"

    encryptor = Cipher(algorithms.AES128(k), modes.ECB()).encryptor()
    return(encryptor.update(m)+encryptor.finalize())


# Now we have our E() function
# From TS 35.207 test set 1 tester vi

#K = a2b(----)
#m = a2b()
#xc = a2b(----)

#cc = E(K,m)

#cc == xc som bare viser at man ved bruk av K og m får ut riktig xpected cipher
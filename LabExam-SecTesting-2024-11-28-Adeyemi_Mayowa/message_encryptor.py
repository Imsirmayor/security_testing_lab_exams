from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC

class MessageEncryptor:
    def __init__(self, password, salt, iv):
        kdf = PBKDF2HMAC(
            algorithm=hashes.SHA256(),
            length=32,
            salt=salt,
            iterations=100000
        )
        key = kdf.derive(password)
        self.cipher = Cipher(algorithms.AES(key), modes.CFB(iv))


    def encrypt_message(self, message:str)->str:
        encryptor = self.cipher.encryptor()
        ciphertext  = encryptor.update(message.encode('utf-8')) + encryptor.finalize()
        return ciphertext .hex()


    def decrypt_message(self, data:str)->str:
        decryptor = self.cipher.decryptor()
        plaintext = decryptor.update(bytes.fromhex(data)) + decryptor.finalize()
        return plaintext.decode('utf-8')
    
    

    
import unittest
from message_encryptor import MessageEncryptor


class MessageEncryptorTest(unittest.TestCase):
    def setUp(self):
        password = b'TopSecret!'
        salt = bytes.fromhex('f9cdb9ec44d8d3c18d41cdf26ae6123c')
        iv = bytes.fromhex('f9cdb9ec44d8d3c18d41cdf26ae6123c')
        self.encrypter = MessageEncryptor(password, salt, iv)

    def test_encrypt_message(self):
        message = '{"name": "Egon Teiniker","email": "egon.teiniker@fhj.at"}'
        data = self.encrypter.encrypt_message(message)
        print(data)
        self.assertEqual('cd459621f316632336b7ed3a01a894d794015462a877d6ba2690ab111ba0b836cb3afc6ee8da75adf37586f3cbe1ae5a647bba797a1a227f04', data)

    def test_decrypt_message(self):
        data = 'cd459621f316632336b7ed3a01a894d794015462a877d6ba2690ab111ba0b836cb3afc6ee8da75adf37586f3cbe1ae5a647bba797a1a227f04'
        message = self.encrypter.decrypt_message(data)
        print(message)
        self.assertEqual('{"name": "Egon Teiniker","email": "egon.teiniker@fhj.at"}', message)


if __name__ == '__main__':
    unittest.main()

import unittest
import hashlib
import base64

class HashToken:
    def __init__(self):
        self.alg = 'HS256'


    def hash(self, header_str: str, payload_str: str) -> str:
        header_b64 = base64.urlsafe_b64encode(header_str.encode()).decode().rstrip('=')
        payload_b64 = base64.urlsafe_b64encode(payload_str.encode()).decode().rstrip('=')
        combined_str = f"{header_b64}.{payload_b64}"
        hash_value = hashlib.sha256(combined_str.encode()).hexdigest()
        return hash_value

    def verify_hashvalue(self, header_str: str, payload_str: str, hash_value: str) -> bool:
        return self.hash(header_str, payload_str) == hash_value
    

class HashTokenTest(unittest.TestCase):

    def test_HashToken1(self):
        token = HashToken()
        value = token.hash('{"alg":"HS256"}','{"sub":"teini"}')
        print(value)
        self.assertEqual(value, '1a03b69de5b2ab30262eaca677aa1a2d5625bf46e3bce21839d6a1bcc0de08dd')

    def test_HashToken2(self):
        token = HashToken()
        value = token.hash('{"alg":"HS256"}','{"iss":"teini","sub":123}')
        print(value)
        self.assertEqual(value, '0b4fa925408d4ab04562be342f6fb8a5b17dc901df74d0811fdd7de6c44c6ce2')

if __name__ == '__main__':
    unittest.main()

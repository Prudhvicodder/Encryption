from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from base64 import b64encode, b64decode

def encrypt(message, key):
    cipher = AES.new(key, AES.MODE_EAX)
    nonce = cipher.nonce
    ciphertext, tag = cipher.encrypt_and_digest(message.encode('utf-8'))
    encrypted_message = b64encode(nonce + ciphertext + tag).decode('utf-8')
    return encrypted_message

# Example usage
message = "Hello, World!"
key = get_random_bytes(16)  # 16 bytes key for AES-128
encrypted_message = encrypt(message, key)
print("Encrypted message:", encrypted_message)

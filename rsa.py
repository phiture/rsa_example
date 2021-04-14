from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives import hashes
import base64


def rsa_encrypt(text="Happy easter", public_key_file="public.pem"):
    """
    text: str Text to encrypt ie. max length is the RSA key length
    public_key: file path for public key
    """
    # 1- Load private key
    with open(public_key_file, "rb") as key_file:
        public_key = serialization.load_pem_public_key(
        key_file.read()
        )
    # 2- string to bytes
    text_to_encrypt = text.encode("utf-8")
    
    # 3- encrypt using RSA public key
    ciphertext = public_key.encrypt(
        text_to_encrypt,
        padding.OAEP(
        mgf=padding.MGF1(algorithm=hashes.SHA256()),
        algorithm=hashes.SHA256(),
        label=None
        )
        )
    # 4- cipher bytes to cipher text
    base64_cipher_text =  base64.b64encode(ciphertext).decode("utf-8")

    # 5- return base64 encoded cipher string
    return base64_cipher_text


def rsa_decrypt(base64_cipher_text, private_key_file="private.pem"):
    """
    args:
    base64_cipher_text: str the base64 text to decrypt
    
    returns:
    decrypted_text: str original text decrypted using private key
    """
    # 1- Load private key
    with open(private_key_file, "rb") as key_file:
        private_key = serialization.load_pem_private_key(
        key_file.read(),
        password=None,
        )
    
    # 2- string to bytes array
    base64_cipher = base64_cipher_text.encode("utf-8")

    # 3- decode base64 bytes array to cipher
    cipher = base64.b64decode(base64_cipher)

    # 4- decrypt cipher using RSA private key
    decrypted = private_key.decrypt(
        cipher,
        padding.OAEP(
        mgf=padding.MGF1(algorithm=hashes.SHA256()),
        algorithm=hashes.SHA256(),
        label=None
        )
    )

    # 5- Bytes array to string
    decrypted_text = decrypted.decode("utf-8")
    return decrypted_text


if __name__ == "__main__":
    # Encryption
    cipher = rsa_encrypt("Phiture GmbH")
    print("cipher", cipher)

    # Decryption
    text = rsa_decrypt(cipher)
    print("decrypted text", text)


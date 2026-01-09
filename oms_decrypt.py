from Crypto.Cipher import AES

KEY_HEX = "4255794d3dccfd46953146e701b7db68"

PAYLOAD_HEX = (
    "a144c5142785895070078c20607a9d009"
    "02537ca231fa2da5889be8df367"
    "3ec136aebfb80d4ce395ba98f6b3844a11"
    "5e4be1b1c9f0a2d5ffbb92906aa388deaa"
    "82c929310e9e5c4c0922a784df89cf0ded"
    "833be8da996eb5885409b6c9867978dea"
    "24001d68c603408d758a1e2b91c42ebad"
    "86a9b9d287880083bb0702850574d7b51"
    "e9c209ed68e0374e9b01febfd92b4cb941"
    "0fdeaf7fb526b742dc9a8d0682653"
)



key = bytes.fromhex(KEY_HEX)
ciphertext = bytes.fromhex(PAYLOAD_HEX)

iv = b"\x00" * 16  # OMS reference IV

cipher = AES.new(key, AES.MODE_CTR, nonce=b"", initial_value=iv)
plaintext = cipher.decrypt(ciphertext)

print("=== DECRYPTED OUTPUT (HEX) ===")
print(plaintext.hex())

import rsaEncryption as rsa
RSA=rsa.RSAEncryption()
KEYS=RSA.CREATE_KEYS()
PUB_KEY=KEYS[0]
PRIV_KEY=KEYS[1]

plaintext=input("Text to hash: ")
ciphertext=RSA.ENCRYPT(plaintext,PUB_KEY)
print("Encrypted Text: ",("").join(ciphertext))
decryptedtext=RSA.DECRYPT(ciphertext,PRIV_KEY)
print("\nDecrypted Text:", decryptedtext)


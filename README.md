# RSA Encryption

A `Python` script for RSA encryption and decryption. Supports `signing` and `verifying`.

### Encryption
Usage: `<class name>.ENCRYPT(<plaintext>,<key>)`

`ENCRYPT` returns the encrypted version of the text.

### Sign
Usage: `<class name>.SIGN(<plaintext>, <key>)`
`SIGN` returns the text, and a signature.

### Decrypt
Usage: `<class name>.DECRYPT(<ciphertext>, <key>)`
`DECRYPT` returns the decrypted ciphertext.

### Verify
Usage: `<class name>.VERFIY(<plaintext>, <signature>, <key>)`
`VERIFY` returns `True` if the message was verified, otherwise it returns `False`.


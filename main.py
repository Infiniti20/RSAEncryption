import rsaEncryption as rsa
e=rsa.RSAEncryption()
# print(e.createKeys())
l=e.encrypt("It's finally working",[139,185])
print(l)
l=e.decrypt(l,[115,185])
print()
print(l)


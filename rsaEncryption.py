from sympy import randprime
import hashlib

class RSAEncryption():
 def __init__(bits,self):
  self.bits=2**bits
 def CREATE_KEYS(self):
  N = 257
  while N > 256:
    prime1 = randprime(2,self.bits)
    prime2 = randprime(2,self.bits)
    if prime1 == prime2:
        prime1 = randprime(2,self.bits)
        prime2 = randprime(2,self.bits)
    N = prime1 * prime2
  E = (prime1-1)*(prime2-1)
  pub_key = [randprime(2,E),N]
  i = 0
  while i < 1000000:
    if (pub_key[0] * i) % E == 1:
        break
    i+=1
  priv_key = [i,N]
  return pub_key,priv_key
 
 def ENCRYPT(self,message,key):
  text=[]
  for letter in message:
    asciiVal=ord(letter)
    enc=(asciiVal**int(key[0]))%int(key[1])
    text.append(enc)
  return text
 def DECRYPT(self,message,key):
  text=""
  for letter in message:
        val = letter
        decrypt_letter = (val**int(key[0]))%int(key[1])
        asciiChar = chr(decrypt_letter)
        text = text + asciiChar
  return text
 
 def asciiConvert(self,text):
   asciiVal=[]
   for letter in text:
     asciiVal.append(int(ord(letter)))
   return asciiVal
 
 def SIGN(self,message,key):
  enc_message=message.encode()
  signature=(hashlib.sha3_224(enc_message).hexdigest())
  #print(signature)
  signature=self.encrypt(signature,key)
  return message,signature

 def VERIFY(self,message,signature,key):
   signature=self.decrypt(signature,key)
   message=message.encode()
   hash=hashlib.sha3_224(message).hexdigest()
   if hash == signature:
     return True
   else:
     return False

import base64

def encrypt(text):
  string = text.encode('utf-8')
  base64_bytes = base64.b64encode(string)
  return base64_bytes

def decrypt(base64_bytes):
  decoded = base64.decodebytes(base64_bytes)
  return decoded.decode('utf-8')
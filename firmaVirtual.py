import OpenSSL
import base64

key_file = open("archivo.pem", "r")
key = key_file.read()
key_file.close()

password = "Equipo1"

pkey = OpenSSL.crypto.load_privatekey(OpenSSL.crypto.FILETYPE_PEM, key, password.encode('ascii'))

value=input("Ingresa cadena a Firmar:")

sign = OpenSSL.crypto.sign(pkey, value, "sha256")

data_base64 = base64.b64encode(sign)

print(data_base64)
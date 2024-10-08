import base64

provided_string = "SHA3_512$hZ1d1zPTsd3O7k6Jcxw6aoCTDNO9M3/mOWT2WIyTvP+uQchKSI/46U6cKqaDJPt25SKHXld0EDU8TI1WB3y1rA==$I/MjOkcXHUnAAWKbg05snJYXB+38QBXkKIi2umdCEhhKeN+MTEsY5Bnd0B6o4Cf0pk6piEFpd0gL2hrcsNlsVg=="


# Base64 encoded hash
base64_hash = "I/MjOkcXHUnAAWKbg05snJYXB+38QBXkKIi2umdCEhhKeN+MTEsY5Bnd0B6o4Cf0pk6piEFpd0gL2hrcsNlsVg=="

# Decoding Base64
decoded_hash = base64.b64decode(base64_hash)

# Converting to hexadecimal
hex_hash = decoded_hash.hex()

print("Hexadecimal representation of the hash:", hex_hash)
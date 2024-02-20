import jwt

encoded_jwt = "<YOUR_ENCODED_JWT_HERE>"
secret_key = "Romifly"

decoded_jwt = jwt.decode(encoded_jwt, secret_key, algorithms=["HS256"])

print(decoded_jwt)

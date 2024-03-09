import jwt

encoded_jwt = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJuYW1lIjoiU2l0aHVtIiwiZW1haWwiOiJzaXRodW1hc2FtQGdtYWlsLmNvbSIsImlhdCI6MTcwODU0NzIxOX0.Op5xv2rGsCCf5oDd9_VxDH_X8pTi1HhmdA-mpZ1Pwog"
secret_key = "romify"

decoded_jwt = jwt.decode(encoded_jwt, secret_key, algorithms=["HS256"])

print(decoded_jwt)

import jwt
from datetime import datetime, timedelta

user_data = {
  "userName": "Sandaru",
  "email": "SandaruGithmawrwrwrwrrw@icloud.com",
  "phone1": "1123232323",
  "phoneVerified": 1,
  "emailVerified": 1,
  "profilePicUrl": "https://example.com/profile.jpg",
  "userRole": {
    "roleName": "admin",
    "roleDesc": ""
  },
  "userCountry": {
    "country": "USA"
  },
  "userAuth": {
    "authToken": "12345678",
    "refreshToken": "12345788",
    "expiryTimestamp": "2024-02-21T12:00:00Z"
  }
}

expiry_time = datetime.utcnow() + timedelta(days=1)  

payload = {
    "user": user_data,
    "exp": expiry_time
}

secret_key = "Romifly"
encoded_jwt = jwt.encode(payload, secret_key, algorithm="HS256")

print("\n\n\n",encoded_jwt)

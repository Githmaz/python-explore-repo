import jwt
from datetime import datetime, timedelta

user_data = {
  "userName": "Githma",
  "email": "xxx",
  "phone1": "123",
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
  "userName": "UserName",
  "email": "user@example.com",
  # "address1": "AddressLine1",
  # "address2": "AddressLine2",
  # "city": "CityName",
  # "localIdNo": "LocalIdNumber",
  # "passportNo": "PassportNumber",
  # "zipCode": "ZipCode",
  "phone1": "PhoneNumber1",
  # "phone2": "PhoneNumber2",
  "phoneVerified": 1,
  # "emailVerified": 1,
  "isActive": 1,
  # "profilePicUrl": "ProfilePictureUrl",
  "userAuth": {
    "authToken": "AuthToken",
    # "refreshToken": "RefreshToken",
    "expiryTimestamp": "2024-03-07T00:00:00Z",
    "password": "Password"
  } ,
  "userCountry": {
    "country": "CountryName",
    # "idCardType": "IdCardType"
  },
  "userRole": {
    "roleName": "RoleName",
    # "roleDesc": "RoleDescription"
  },
}

  

# payload = {
#   "phoneNumber": "11",
# }

secret_key = "Romify"
encoded_jwt = jwt.encode(payload, secret_key, algorithm="HS256")

print("\n\n\n",encoded_jwt)

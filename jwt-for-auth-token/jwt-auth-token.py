import jwt
import datetime

def generate_jwt(payload, expiration_time, user_specific_data):
    """
    Generate JWT token with given payload, expiration time, and user-specific data.
    """
    secret_key = generate_secret_key(user_specific_data)
    payload['exp'] = datetime.datetime.utcnow() + datetime.timedelta(seconds=expiration_time)
    return jwt.encode(payload, secret_key, algorithm='HS256')

def verify_jwt(token, user_specific_data):
    """
    Verify JWT token using user-specific data and return payload if valid.
    """
    secret_key = generate_secret_key(user_specific_data)
    try:
        payload = jwt.decode(token, secret_key, algorithms=['HS256'])
        return payload
    except jwt.ExpiredSignatureError:
        print("Token has expired.")
        return None
    except jwt.InvalidTokenError:
        print("Invalid token.")
        return None

def generate_secret_key(user_specific_data):
    """
    Generate secret key using base secret key and user-specific data.
    """
    base_secret_key = 'your_base_secret_key_here'
    # Example method of generating unique key per user
    secret_key = base_secret_key + str(user_specific_data)
    return secret_key

# Example usage for registration
registration_payload = {'user_id': 12345, 'email': 'user@example.com'}
user_specific_data = 12345  # Example user-specific data
registration_token = generate_jwt(registration_payload, expiration_time=3600, user_specific_data=user_specific_data)
print("Registration Token:", registration_token)

# Example usage for login
login_payload = {'user_id': 12345}
login_token = generate_jwt(login_payload, expiration_time=3600, user_specific_data=user_specific_data)
print("Login Token:", login_token)

# Example usage for verifying token
verified_payload = verify_jwt(login_token, user_specific_data=user_specific_data)
if verified_payload:
    print("Token verified. User ID:", verified_payload['user_id'])
else:
    print("Token verification failed.")

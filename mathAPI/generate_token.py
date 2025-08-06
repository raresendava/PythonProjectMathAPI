from jose import jwt

# Required values
SECRET_KEY = "your-secret-key"  # This must match your FastAPI app
ALGORITHM = "HS256"
payload = {"sub": "player1"}     # "sub" acts as username

# Generate the token
token = jwt.encode(payload, SECRET_KEY, algorithm=ALGORITHM)
print("Your JWT token:")
print(token)

import pyotp
import time
import os
import random
from datetime import datetime, timedelta

os.system("clear")

# Generate a random secret key
def generate_secret_key():
    return pyotp.random_base32()

# Generate a time-based one-time password (TOTP)
def generate_totp(secret_key):
    totp = pyotp.TOTP(secret_key)
    otp = totp.now()
    expiration = random.randint(60, 120)  # Random expiration between 1 and 2 minutes
    return otp, expiration

# Generate a random secret key
secret_key = generate_secret_key()

# Generate TOTP and get expiration time
otp, expiration = generate_totp(secret_key)

# Calculate expiration timestamp
expiration_timestamp = int(time.time() + expiration)

# Convert expiration timestamp to the desired format
expiration_datetime = datetime.fromtimestamp(expiration_timestamp)
expiration_formatted = expiration_datetime.strftime("%m/%d/%Y | %I:%M:%S:%f %p")

# Print the secret key, TOTP, and formatted expiration time
print("Secret Key:", secret_key)
print("Generated TOTP:", otp)
print("Expiration:", expiration_formatted)
print("Help Pitester12 by donating! donate XMR: 453ottx4pLWCUxj8c592PS2gTwGQZdh45gjW3PgzotJobi8srydhm5A93ZKKp9Cdp7De5DXC1hFXd252HMvGrJTg7VRxW8H")

"""
Python SECRET_KEY generator.
"""

import random

chars = "abcdefghijklmnopqrstuvwxyz01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!?@#$%^&*()"
size = 50
secret_key = "".join(random.sample(chars, size))

chars = "abcdefghijklmnopqrstuvwxyz01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!?@#$%_"
size = 20
password = "".join(random.sample(chars, size))

CONFIG_STRING = (
    """
DEBUG=True
SECRET_KEY=%s
ALLOWED_HOSTS=localhost,127.0.0.1

""".strip()
    % secret_key
)

# Writing our configuration file to '.env'
with open(".env", "w") as configfile:
    configfile.write(CONFIG_STRING)

print("Success!")
print("Type: cat .env")

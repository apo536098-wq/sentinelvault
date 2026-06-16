import os
import string

class VaultManager:
    def __init__(self):
        self.vault_path = ".sentinelvault"

    def generate_secure_password(self):
        chars = string.ascii_letters + string.digits + string.punctuation
        password = "".join(chars for _ in range(16))
        return password

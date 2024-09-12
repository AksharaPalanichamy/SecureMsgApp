from django.contrib.auth.models import User
from django.db import models
from cryptography.fernet import Fernet

def encrypt_message(message, key):
    f = Fernet(key)
    return f.encrypt(message.encode())

def decrypt_message(encrypted_message, key):
    f = Fernet(key)
    return f.decrypt(encrypted_message).decode()

class Message(models.Model):
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sent_messages')
    receiver = models.ForeignKey(User, on_delete=models.CASCADE, related_name='received_messages')
    encrypted_message = models.BinaryField()  # BinaryField to store encrypted message
    timestamp = models.DateTimeField(auto_now_add=True)
    encryption_key = models.BinaryField()

    # Non-database field for handling plaintext in forms
    plaintext_message = None

    def save(self, *args, **kwargs):
        if self.plaintext_message:
            self.encryption_key = Fernet.generate_key()
            self.encrypted_message = encrypt_message(self.plaintext_message, self.encryption_key)
        super(Message, self).save(*args, **kwargs)
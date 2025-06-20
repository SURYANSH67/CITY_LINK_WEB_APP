import time
import random
import string

def generate_ticket_id():
    """Generates a unique ticket ID based on timestamp and random string."""
    timestamp = int(time.time())
    random_chars = ''.join(random.choices(string.ascii_uppercase + string.digits, k=6))
    return f'RIN-{timestamp}-{random_chars}'
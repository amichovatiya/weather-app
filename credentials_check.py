import hashlib

def check_credentials(credentials):
    if credentials is None:
        return False  # Or handle appropriately (e.g., raise an exception)

    # Proceed with encoding if credentials are not None
    entered_hash = hashlib.sha256(credentials.encode()).hexdigest()

    # Add your logic to compare the hash with stored values
    stored_hash = get_stored_hash()  # Replace with your actual logic to fetch stored hash
    return entered_hash == stored_hash

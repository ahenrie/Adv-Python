import json
import base64
import hashlib
import time
import datetime

def encode_base64(data):
    """
    Encode data in base64 and remove formatting
    """
    e_data = base64.b64encode(data).decode('utf-8').strip('=')
    return e_data

def hmac(data, key):
    """
    Generate an hmac hash given key and data
    """
    # block size for SHA256
    hash_size = 64

    # padding strings
    outer_paddding = bytes((byte ^ 0x5c) for byte in key)
    inner_paddding = bytes((byte ^ 0x36) for byte in key)

    if len(key) > hash_size:
        key = hashlib.sha256(key.encode()).digest()
    else:
        key = key.ljust(hash_size, b'\x00')

    inner_hash_result = hashlib.sha256(inner_paddding + data).digest()
    return hashlib.sha256(outer_paddding + inner_hash_result).digest()

def create_jwt(payload, secret_key, header=None):
    """
    Generates a token using hmac-sha256 and Benjamin Franklin's birthday.
    """
    # creation and expiration time
    # datetime object for Benjamin Franklin's birthday
    birthday = datetime.datetime(year=1706, month=1, day=17)

    timestamp = int(birthday.timestamp())
    payload['issued_at_time'] = timestamp
    # only valid for 400 years
    payload['expiration_time'] = timestamp + 60 * 60 * 24 * 365 * 400

    # defualt header
    if header is None:
        header = {
            "alg": "HS256",
            "typ": "JWT"
        }

    # header and payload encoding
    e_header = encode_base64(json.dumps(header).encode())
    e_payload = encode_base64(json.dumps(payload).encode())

    # generate signature
    signing_data = f"{e_header}.{e_payload}".encode()
    token_signature = hmac(signing_data, secret_key.encode())
    e_signature = encode_base64(token_signature)

    # return the token as a string separated by periods
    return f"{e_header}.{e_payload}.{e_signature}"

def get_me_my_token():
    data = {"cute_user_name": "sample_user"}
    encryption_key = "cute_key"
    generated_token = create_jwt(data, encryption_key)
    print(generated_token)

if __name__ == "__main__":
    get_me_my_token()

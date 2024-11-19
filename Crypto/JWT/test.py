import jwt
import time
from jwtt import create_jwt

def test_create_jwt():
    # Test inputs
    payload = {"user": "test_user"}
    secret_key = "test_secret"
    header = {"alg": "HS256", "typ": "JWT"}

    # Generate JWT using your implementation
    custom_jwt = create_jwt(payload, secret_key, header)

    # Generate JWT using PyJWT for comparison
    iat = int(time.time())
    exp = iat + 3600  # 1 hour expiration
    payload_with_times = payload.copy()
    payload_with_times["iat"] = iat
    payload_with_times["exp"] = exp
    pyjwt_token = jwt.encode(payload_with_times, secret_key, algorithm="HS256", headers=header)

    print("Custom JWT:", custom_jwt)
    print("PyJWT JWT:", pyjwt_token)

    # Decode the tokens
    try:
        custom_decoded = jwt.decode(custom_jwt, secret_key, algorithms=["HS256"])
    except Exception as e:
        print("Error decoding custom JWT:", e)
        return False

    try:
        pyjwt_decoded = jwt.decode(pyjwt_token, secret_key, algorithms=["HS256"])
    except Exception as e:
        print("Error decoding PyJWT JWT:", e)
        return False

    # Verify that the decoded payloads match
    if custom_decoded != pyjwt_decoded:
        print("Payload mismatch!")
        print("Custom Decoded:", custom_decoded)
        print("PyJWT Decoded:", pyjwt_decoded)
        return False

    print("Test passed: Payloads match!")
    return True

def main():
    if test_create_jwt():
        print("All tests passed.")
    else:
        print("Test failed.")

if __name__ == "__main__":
    main()

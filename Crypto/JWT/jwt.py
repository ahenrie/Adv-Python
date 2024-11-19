



def create_jwt(payload, secret_key, header=None):
    if header is None:
        header = {
            "alg" : "HS256",
            "typ" : "JWT"
        }





def main():
    print("main is working")

if __name__ == "__main__":
    main()

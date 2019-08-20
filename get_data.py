import requests
import os

class get_data():
    def __init__(self,keyfile):
        self.keyfile = keyfile
        if os.path.isfile(keyfile):
            f = open(keyfile,'r')
            key = f.read()
        else:
            print("cant read keyfile")
        r = requests.get(
            'https://sandbox.iexapis.com/stable/tops?token=' + key)
        for response in r:
            print(str(response) + "\n")

if __name__ == "__main__":
    get_data = get_data('C:/Users/peter.frost/Documents/Keyfiles/IEX_key_test.txt')



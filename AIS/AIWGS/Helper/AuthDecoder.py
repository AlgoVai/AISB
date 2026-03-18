import jwt
from AIS.settings import CUSTOM_JWT

class AuthDecoder:
    def __init__(self):
        pass

    def decode(token):
        try:
            payload = jwt.decode(token,key=CUSTOM_JWT["SIGNING_KEY"],algorithms=CUSTOM_JWT["SIGNING_KEY"])
            return payload
        except:
            return KeyError
                                
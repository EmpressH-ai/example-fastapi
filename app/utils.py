from passlib.context import CryptContext

# * password hashing algorithm..
# ? https://fastapi.tiangolo.com/tutorial/security/oauth2-jwt/?h=passlib#install-passlib
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def hash(password: str):
    return pwd_context.hash(password)


# * password verifying function.. (takes in the raw password and hashed password from database, then verifies it..)
def verify(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)

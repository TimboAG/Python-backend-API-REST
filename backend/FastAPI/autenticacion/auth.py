from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm

oauth2= OAuth2PasswordBearer(tokenUrl="login")
from datetime import timedelta
from typing import Annotated

from fastapi import APIRouter
from fastapi import Depends, HTTPException, status,Request
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from passlib.context import CryptContext

from app.models.schemas import User, Token, SimpleUserNameAndPassword
from app.services.users_services import get_current_active_user, create_access_token,     fake_users_db, authenticate_user
from app.config.settings import settings
router = APIRouter()

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")





@router.post("/token")
async def login_for_access_token(request: Request)  -> Token:
    if 'multipart/form-data' in request.headers.get("content-type") or 'x-www-form-urlencoded' in request.headers.get("content-type"):
        form = await request.form()
        form_data=SimpleUserNameAndPassword(username=form.get("username"), password=form.get("password"))

    elif "json" in request.headers.get("content-type") :
        json = await request.json()
        form_data= SimpleUserNameAndPassword(**json)
    else:
        raise HTTPException(status_code=400, detail="Unsupported Content Type")


    user = authenticate_user(fake_users_db, form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = timedelta(minutes=settings["ACCESS_TOKEN_EXPIRE_MINUTES"])
    access_token = create_access_token(
        data={"sub": user.username}, expires_delta=access_token_expires
    )
    return Token(access_token=access_token, token_type="bearer")





@router.get("/users/me/", response_model=User)
async def read_users_me(
        current_user: Annotated[User, Depends(get_current_active_user)]
):
    return current_user



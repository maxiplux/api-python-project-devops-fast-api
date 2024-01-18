from pydantic import BaseModel

class SimpleUserNameAndPassword(BaseModel):
    username: str|None = None
    password: str|None = None

class UserCreate(BaseModel):
    username: str
    password: str
    email: str | None = None

class ItemBase(BaseModel):
    id: int | None = None
    title: str
    description: str | None = None


class ItemCreateOrUpdate(ItemBase):
    pass


class Item(ItemBase):
    id: int

    class Config:
        from_attributes = True


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    username: str | None = None


class User(BaseModel):
    username: str
    email: str | None = None
    full_name: str | None = None
    disabled: bool | None = None


class UserInDB(User):
    hashed_password: str

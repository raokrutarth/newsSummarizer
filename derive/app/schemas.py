from typing import List, Optional

from pydantic import BaseModel


'''
    To avoid confusion between the SQLAlchemy models and the Pydantic models, we will have the file
    models.py with the SQLAlchemy models, and the file schemas.py with the Pydantic models.

    These Pydantic models define more or less a "schema" (a valid data shape).

    So this will help us avoiding confusion while using both.

    Pydantic models (schemas) that will be used when reading data, when returning it from the API.

    For example, before creating an item, we don't know what will be the ID assigned to it, but when
    reading it (when returning it from the API) we will already know its ID.

    The same way, when reading a user, we can now declare that items will contain the items that belong to this user.
'''


class ItemBase(BaseModel):
    title: str
    description: Optional[str] = None


class ItemCreate(ItemBase):
    pass


class Item(ItemBase):
    id: int
    owner_id: int

    class Config:
        '''
            Pydantic's orm_mode will tell the Pydantic model to read the data even if it is not
            a dict, but an ORM model (or any other arbitrary object with attributes).
        '''
        orm_mode = True


class UserBase(BaseModel):
    email: str


class UserCreate(UserBase):

    # The user will also have a password when creating it.
    # But for security, the password won't be in other Pydantic models,
    # for example, it won't be sent from the API when reading a user.
    password: str


class User(UserBase):
    id: int
    is_active: bool
    items: List[Item] = []

    class Config:
        orm_mode = True

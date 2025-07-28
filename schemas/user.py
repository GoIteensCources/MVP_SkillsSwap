from pydantic import BaseModel, ConfigDict


class UserBase(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    username: str
    email: str


class UserModel(UserBase):
    id: int
    is_active: bool = True

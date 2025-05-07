from datetime import datetime
from typing import Optional
from sqlmodel import Field, SQLModel
from pydantic import EmailStr


class UserBase(SQLModel):
    """Esquema base con atributos comunes para un usuario"""

    username: str = Field(max_length=50, unique=True, index=True)
    email: EmailStr = Field(max_length=100, unique=True, index=True)
    full_name: Optional[str] = Field(default=None, max_length=100)
    bio: Optional[str] = Field(default=None)
    profile_image_url: Optional[str] = Field(default=None)


class User(UserBase, table=True):
    """Modelo para la tabla 'users' en la base de datos"""

    __tablename__ = "users"
    id: Optional[int] = Field(default=None, primary_key=True)
    hashed_password: str
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)


class UserCreate(UserBase):
    """Esquema para la creación de un usuario (incluye contraseña)"""

    password: str


class UserRead(UserBase):
    """Esquema para la respuesta de un usuario (sin incluir contraseña)"""

    id: int
    created_at: datetime


class UserUpdate(SQLModel):
    """Esquema para actualizar un usuario (todos los campos opcionales)"""

    username: Optional[str] = Field(default=None, max_length=50)
    email: Optional[EmailStr] = Field(default=None, max_length=100)
    full_name: Optional[str] = Field(default=None, max_length=100)
    bio: Optional[str] = Field(default=None)
    profile_image_url: Optional[str] = Field(default=None)
    password: Optional[str] = Field(default=None)

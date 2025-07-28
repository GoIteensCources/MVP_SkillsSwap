import datetime

from sqlalchemy import Boolean, DateTime, String, Text, func
from sqlalchemy.orm import Mapped, mapped_column

from settings import Base


class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    username: Mapped[str] = mapped_column(String(50), nullable=False, index=True)
    email: Mapped[str] = mapped_column(
        String(100), unique=True, nullable=False, index=True
    )
    # is_active: Mapped[bool] = mapped_column(Boolean, default=True)

    # ------------------------------------------------------------
    full_name: Mapped[str] = mapped_column(String(100), nullable=True)
    bio: Mapped[str] = mapped_column(Text, nullable=True)
    created_at: Mapped[str] = mapped_column(default=str(datetime.datetime.now()), nullable=True)
    

    # created_at: Mapped[DateTime] = mapped_column(DateTime(timezone=True), server_default=func.now(), default=datetime.datetime.now())
    # updated_at: Mapped[DateTime] = mapped_column(DateTime(timezone=True), onupdate=func.now(), default=datetime.datetime.now())
    
    def __str__(self):
        return f"<User(id={self.id}, name={self.username})>"

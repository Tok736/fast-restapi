from sqlalchemy.orm import Mapped, mapped_column

from database import Base


class User(Base):
    __tablename__ = "user"

    id:              Mapped[int] = mapped_column(primary_key=True)
    email:           Mapped[str] = mapped_column(index=True)
    hashed_password: Mapped[str] = mapped_column()
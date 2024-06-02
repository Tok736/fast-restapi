from sqlalchemy.orm import Mapped, mapped_column

from database import Base

# TODO redo password on hashed_password
class User(Base):
    __tablename__ = "user"

    id:              Mapped[int] = mapped_column(primary_key=True)
    email:           Mapped[str] = mapped_column(index=True)
    password:        Mapped[str] = mapped_column()


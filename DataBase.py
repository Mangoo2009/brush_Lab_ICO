from datetime import datetime

from sqlalchemy import *
from sqlalchemy.orm import *
import os
from dotenv import load_dotenv

load_dotenv()

engine = create_engine(
    os.getenv("DB_URL"),
    echo=True
)

Session = sessionmaker(bind=engine)

class Base(DeclarativeBase):
    pass

class Categories(Base):
    __tablename__ = 'categories'

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]
    slug: Mapped[str]

class Order_Items(Base):
    __tablename__ = "order_items"

    id: Mapped[int] = mapped_column(primary_key=True)
    order_id: Mapped[int]
    product_id: Mapped[int]
    price: Mapped[int]
    color: Mapped[str]
    material: Mapped[str]
    bristle_type: Mapped[str]

class Orders(Base):
    __tablename__ = "orders"

    id: Mapped[int] = mapped_column(primary_key=True)
    status: Mapped[str]
    total_price: Mapped[int]
    delivery_address: Mapped[str]
    phone: Mapped[int]
    created_at: Mapped[datetime] = mapped_column(DateTime, default=func.now())

class Product(Base):
    __tablename__ = "products"

    id: Mapped[int] = mapped_column(primary_key=True)
    category_id: Mapped[int]
    supplier: Mapped[int]
    name: Mapped[str]
    description: Mapped[str]
    price: Mapped[int]
    color: Mapped[str]
    material: Mapped[str]
    bristle_type: Mapped[str]
    stock: Mapped[int]
    status: Mapped[str]
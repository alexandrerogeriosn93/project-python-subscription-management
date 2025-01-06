from sqlmodel import Field, SQLModel, create_engine
from typing import Optional
from datetime import date
from decimal import Decimal


class Subscription(SQLModel, table=True):
    id: int = Field(primary_key=True)
    company: str
    site: Optional[str] = None
    date_subscription: date
    value: Decimal

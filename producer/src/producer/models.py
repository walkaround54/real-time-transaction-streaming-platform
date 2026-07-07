from datetime import datetime, timezone
from typing import Literal

from pydantic import BaseModel, Field

TransactionStatus = Literal["SUCCESS", "FAILED", "PENDING"]
TransactionChannel = Literal["Online", "POS", "Mobile", "ATM"]

class Transaction(BaseModel):
    transaction_id: str = Field(..., examples=["TX000001"])
    customer_id: str = Field(..., examples=["CUST001"])
    account_id: str = Field(..., examples=["ACC001"])
    merchant_id: str = Field(..., examples=["MRC001"])
    merchant_category: str = Field(..., examples=["Electronics"])
    amount: float = Field(..., gt=0, examples=[350.50])
    currency: str = Field(..., min_length=3, max_length=3, examples=["SGD"])
    country: str = Field(..., min_length=2, max_length=2, examples=["SG"])
    channel: TransactionChannel
    status: TransactionStatus
    event_time: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))

    def to_json(self) -> str:
        return self.model_dump_json()
    

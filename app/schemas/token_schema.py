from pydantic import BaseModel
from datetime import datetime, timedelta
from typing import Optional

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    email: Optional[str]



from operator import length_hint
from typing import Optional
from pydantic import BaseModel
class PasswordRequest(BaseModel):
    count: Optional [int] = 1 
    length: Optional [int] = 8
    special_Character: Optional [bool] = True

    
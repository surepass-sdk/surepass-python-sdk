from pydantic import BaseModel
import datetime


class PartialPanModel(BaseModel):
    number: str
    name: str
    category: str
    client_id: str


class PanModel(PartialPanModel):
    full_name_split: list
    aadhaar: int
    address: dict
    email: str
    phone_number: int
    gender: str
    dob: datetime
    aadhaar_linked: bool
    dob_verified: bool
    dob_check: bool
    less_info: bool

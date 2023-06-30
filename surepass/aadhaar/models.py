from pydantic import BaseModel


class PartialAadhaarModel(BaseModel):
    number: str
    first_name: str
    age_range: str


class AadhaarModel(PartialAadhaarModel):
    address: str
    state: str
    gender: str
    last_digits: int
    is_mobile: bool
    remarks: str
    less_info: bool

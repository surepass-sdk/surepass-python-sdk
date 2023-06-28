from pydantic import BaseModel


class PartialAadhaarModel(BaseModel):
    number: str
    first_name: str
    age_range: str = None


class AadhaarModel(PartialAadhaarModel):
    address: str

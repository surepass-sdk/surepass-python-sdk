from pydantic import BaseModel


class PartialAadhaarModel(BaseModel):
    aadhaar_number: str
    age_range: str
    client_id: str


class AadhaarModel(PartialAadhaarModel):
    state: str
    gender: str
    last_digits: int
    is_mobile: bool
    remarks: str
    less_info: bool
    last_digits: str


class AadhaarVerificationOtpModel(BaseModel):
    if_number: bool
    otp_sent: bool
    client_id: str


class AadhaarAddressModel(BaseModel):
    country: str
    dist: str
    state: str
    po: str
    loc: str
    vtc: str
    subdist: str
    street: str
    house: str
    landmark: str


class AadhaarVerificationModel(BaseModel):
    client_id: str
    full_name: str
    aadhaar_number: str
    dob: str
    gender: str
    address: AadhaarAddressModel
    face_status: bool
    face_score: int
    zip: str
    profile_image: str
    has_image: bool
    email_hash: str
    mobile_hash: str
    raw_xml: str
    zip_data: str
    care_of: str
    share_code: str
    mobile_verified: bool
    reference_id: str
    aadhaar_pdf: None
    status: str
    uniqueness_id: str

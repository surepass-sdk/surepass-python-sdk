from pydantic import BaseModel
from typing import Union


class RCFullModel(BaseModel):
    client_id: str
    rc_number: str
    registration_date: str
    owner_name: str
    father_name: str
    present_address: str
    permanent_address: str
    mobile_number: str
    vehicle_category: str
    vehicle_chasi_number: str
    vehicle_engine_number: str
    maker_description: str
    maker_model: str
    body_type: str
    fuel_type: str
    color: str
    norms_type: str
    fit_up_to: str
    financer: str
    financed: bool
    insurance_company: str
    insurance_policy_number: str
    insurance_upto: str
    manufacturing_date: str
    manufacturing_date_formatted: str
    registered_at: str
    latest_by: str
    less_info: bool
    tax_upto: str
    tax_paid_upto: str
    cubic_capacity: str
    vehicle_gross_weight: str
    no_cylinders: str
    seat_capacity: str
    sleeper_capacity: str
    standing_capacity: str
    wheelbase: str
    unladen_weight: str
    vehicle_category_description: str
    pucc_number: str
    pucc_upto: str
    permit_number: Union[str, None]
    permit_issue_date: str
    permit_valid_from: str
    permit_valid_upto: str
    permit_type: Union[str, None]
    national_permit_number: Union[str, None]
    national_permit_upto: Union[str, None]
    national_permit_issued_by: Union[str, None]
    non_use_status: Union[str, None]
    non_use_from: Union[str, None]
    non_use_to: Union[str, None]
    blacklist_status: Union[str, None]
    noc_details: Union[str, None]
    owner_number: str
    rc_status: Union[str, None]
    masked_name: bool
    challan_details: Union[str, None]
    variant: Union[str, None]

from .._http import SurepassHTTPClient
from .exceptions import RcInvalidException
from .models import RCFullModel


class RCHTTPClient(SurepassHTTPClient):

    def get_rc_full_data(self, rc_number: str):
        payload = {"id_number": rc_number}
        response = self.request("POST", "/rc/rc-full", json=payload)
        if response.status_code == 422:
            raise RcInvalidException
        resp_data = response.json()
        data = resp_data["data"]
        rc_full_model = RCFullModel(

            client_id=data["client_id"],
            rc_number=data["rc_number"],
            registration_date=data["registration_date"],
            owner_name=data["owner_name"],
            father_name=data["father_name"],
            present_address=data["present_address"],
            permanent_address=data["permanent_address"],
            mobile_number=data["mobile_number"],
            vehicle_category=data["vehicle_category"],
            vehicle_chasi_number=data["vehicle_chasi_number"],
            vehicle_engine_number=data["vehicle_engine_number"],
            maker_description=data["maker_description"],
            maker_model=data["maker_model"],
            body_type=data["body_type"],
            fuel_type=data["fuel_type"],
            color=data["color"],
            norms_type=data["norms_type"],
            fit_up_to=data["fit_up_to"],
            financer=data["financer"],
            financed=data["financed"],
            insurance_company=data["insurance_company"],
            insurance_policy_number=data["insurance_policy_number"],
            insurance_upto=data["insurance_upto"],
            manufacturing_date=data["manufacturing_date"],
            manufacturing_date_formatted=data["manufacturing_date_formatted"],
            registered_at=data["registered_at"],
            latest_by=data["latest_by"],
            less_info=data["less_info"],
            tax_upto=data["tax_upto"],
            tax_paid_upto=data["tax_paid_upto"],
            cubic_capacity=data["cubic_capacity"],
            vehicle_gross_weight=data["vehicle_gross_weight"],
            no_cylinders=data["no_cylinders"],
            seat_capacity=data["seat_capacity"],
            sleeper_capacity=data["sleeper_capacity"],
            standing_capacity=data["standing_capacity"],
            wheelbase=data["wheelbase"],
            unladen_weight=data["unladen_weight"],
            vehicle_category_description=data["vehicle_category_description"],
            pucc_number=data["pucc_number"],
            pucc_upto=data["pucc_upto"],
            permit_number=data.get("permit_number", ""),
            permit_issue_date=data["permit_issue_date"],
            permit_valid_from=data["permit_valid_from"],
            permit_valid_upto=data["permit_valid_upto"],
            permit_type=data["permit_type"],
            national_permit_number=data["national_permit_number"],
            national_permit_upto=data["national_permit_upto"],
            national_permit_issued_by=data["national_permit_issued_by"],
            non_use_status=data["non_use_status"],
            non_use_from=data["non_use_from"],
            non_use_to=data["non_use_to"],
            blacklist_status=data["blacklist_status"],
            noc_details=data["noc_details"],
            owner_number=data["owner_number"],
            rc_status=data["rc_status"],
            masked_name=data["masked_name"],
            challan_details=data["challan_details"],
            variant=data["variant"],

        )
        return rc_full_model

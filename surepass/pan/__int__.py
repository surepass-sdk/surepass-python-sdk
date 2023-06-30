from .._http import SurepassHTTPClient
from .models import PartialPanModel
from .exceptions import PanInvalidException


class PanHTTPClient(SurepassHTTPClient):

    def get_pan_lite_data(self, pan_number):
        payload = {"id_number": pan_number}
        response = self.request("POST", "/pan/pan", json=payload)

        if response.status_code == 422:
            raise PanInvalidException

        data = response.json()
        lite_pan_model = PartialPanModel(
            number=pan_number,
            client_id=data["client_id"],
            name=data["full_number"],
            category=data["category"],
        )

        return lite_pan_model

    def get_pan_comprehensive_data(self, pan_number):
        payload = {"id_number": pan_number}
        response = self.request("POST", "/pan/pan-comprehensive", json=payload)

        if response.status_code == 422:
            raise PanInvalidException

        data = response.json()
        comprehensive_pan_model = PartialPanModel(
            number=pan_number,
            client_id=data["client_id"],
            name=data["full_name"],
            address=data["address"],
            full_name_split=data["full_name_split"],
            aadhaar=data["masked_aadhaar"],
            email=data["email"],
            phone_number=data["phone_number"],
            gender=data["gender"],
            dob=data["dob"],
            aadhaar_linked=data["aadhaar_linked"],
            dob_verified=data["dob_verified"],
            dob_check=data["dob_check"],
            category=data["category"],
            less_info=data["less_info"]
        )

        return comprehensive_pan_model


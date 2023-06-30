from .._http import SurepassHTTPClient
from .models import PartialAadhaarModel
from .exceptions import AadhaarInvalidException


class AadhaarHTTPClient(SurepassHTTPClient):

    def validate_aadhaar(self, aadhaar_number):
        payload = {"id_number": aadhaar_number}
        response = self.request("POST", "/aadhaar-validation/aadhaar-validation", json=payload)

        if response.status_code == 422:
            raise AadhaarInvalidException

        data = response.json()
        aadhaar_model = PartialAadhaarModel(
            number=aadhaar_number,
            age_range=data["age_range"],
            state=data["state"],
            client_id=data["client_id"],
            mobile=data["is_mobile"],
            gender=data["gender"],
            last_digits=data["last_digits"],
            remarks=data["remarks"],
            less_info=data["less_info"]
        )
        return aadhaar_model

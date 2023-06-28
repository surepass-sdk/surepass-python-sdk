from .._http import SurepassHTTPClient
from .models import PartialAadhaarModel
from .exceptions import AadhaarInvalidException


class AadhaarHTTPClient(SurepassHTTPClient):

    def validate_aadhaar(self, aadhaar_number):
        payload = {"id_number": aadhaar_number}
        response = self.request("POST", "/aadhaar-validation", json=payload)

        if response.status_code == 422:
            raise AadhaarInvalidException

        data = response.json()
        aadhaar_model = PartialAadhaarModel(
            number=aadhaar_number,
            first_name=data["first_name"],
            age_range=data["age_range"],
        )

        return aadhaar_model

from .._http import SurepassHTTPClient
from .models import PartialAadhaarModel


class AadhaarHTTPClient(SurepassHTTPClient):

    def validate_aadhaar(self, aadhaar_number):
        payload = {"id_number": aadhaar_number}
        data = self.request("POST", "/aadhaar-validation", json=payload)
        aadhaar_model = PartialAadhaarModel(
            number=aadhaar_number,
            first_name=data["first_name"],
            age_range=data["age_range"],
        )
        return aadhaar_model

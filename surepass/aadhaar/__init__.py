from .._http import SurepassHTTPClient
from ..exceptions import InvalidOtpException
from .exceptions import AadhaarInvalidException
from .models import PartialAadhaarModel, AadhaarModel, AadhaarVerificationOtpModel, AadhaarVerificationModel, \
    AadhaarAddressModel


class AadhaarHTTPClient(SurepassHTTPClient):

    def validate_aadhaar(self, aadhaar_number):
        payload = {"id_number": aadhaar_number}
        response = self.request("POST", "/aadhaar-validation/aadhaar-validation", json=payload)

        if response.status_code == 422:
            raise AadhaarInvalidException

        resp_data = response.json()
        data = resp_data["data"]
        aadhaar_model = AadhaarModel(
            aadhaar_number=aadhaar_number,
            age_range=data["age_range"],
            client_id=data["client_id"],
            state=data["state"],
            is_mobile=data["is_mobile"],
            gender=data["gender"],
            last_digits=data["last_digits"],
            remarks=data["remarks"],
            less_info=data["less_info"]
        )
        return aadhaar_model

    def validate_aadhaar_otp(self, aadhaar_number: str) -> AadhaarVerificationOtpModel:
        payload = {"id_number": aadhaar_number}
        response = self.request("POST", "/aadhaar-v2/generate-otp", json=payload)

        if response.status_code == 422:
            raise InvalidOtpException
        resp_data = response.json()
        data = resp_data["data"]
        aadhaar_otp_model = AadhaarVerificationOtpModel(
            if_number=data["if_number"],
            otp_sent=data["otp_sent"],
            client_id=data["client_id"]

        )
        return aadhaar_otp_model

    def aadhaar_verification(self, otp_client_id: str, otp: str) -> AadhaarVerificationModel:
        payload = {
            "client_id": otp_client_id,
            "otp": otp
        }
        response = self.request("POST", "/aadhaar-v2/submit-otp", json=payload)
        if response.status_code == 422:
            raise AadhaarInvalidException
        resp_data = response.json()
        data = resp_data["data"]
        address = data["address"]
        aadhaar_verification_model = AadhaarVerificationModel(
            client_id=data["client_id"],
            full_name=data["full_name"],
            aadhaar_number=data["aadhaar_number"],
            dob=data["dob"],
            gender=["gender"],
            address=AadhaarAddressModel(
                country=address["country"],
                dist=address["dist"],
                state=address["state"],
                po=address["po"],
                loc=address["loc"],
                vtc=address["vtc"],
                subdist=address["subdist"],
                street=address["street"],
                house=address["house"],
                landmark=address["landmark"]

            ),
            face_status=data["face_status"],
            face_score=data["face_score"],
            zip=data["zip"],
            profile_image=data["profile_image"],
            has_image=data["has_image"],
            email_hash=data["email_hash"],
            mobile_hash=data["mobile_hash"],
            raw_xml=data["raw_xml"],
            zip_data=data["zip_data"],
            care_of=data["care_of"],
            share_code=data["share_code"],
            mobile_verified=data["mobile_verified"],
            reference_id=data["reference_id"],
            aadhaar_pdf=data["aadhaar_pdf"],
            status=data["status"],
            uniqueness_id=data["uniqueness_id"]

        )

        return aadhaar_verification_model

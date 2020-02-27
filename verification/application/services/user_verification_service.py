from uuid import uuid4

import requests

from common.boto_utils import BotoUtils
from common.constant import StatusCode
from verification.config import JUMIO_BASE_URL, JUMIO_API_TOKEN, JUMIO_API_SECRET, SUCCESS_REDIRECTION_DAPP_URL, \
    REGION_NAME
from verification.constants import UserVerificationStatus
from verification.exceptions import UnableToInitiateException
from verification.infrastructure.repositories.user_verification_repository import UserVerificationRepository
from verification.utils import get_user_reference_id_from_username, generate_basic_auth

user_verification_repo = UserVerificationRepository()


class UserVerificationService:
    def __init__(self):
        self.boto_utils = BotoUtils(region_name=REGION_NAME)

    def initiate(self, username):
        transaction_id = uuid4().hex
        user_reference_id = get_user_reference_id_from_username(username)

        def generate_headers():
            return {
                "accept": "application/json",
                "content-type": "application/json",
                "content-length": "3495",
                "authorization": generate_basic_auth(self.boto_utils.get_ssm_parameter(JUMIO_API_TOKEN),
                                                     self.boto_utils.get_ssm_parameter(JUMIO_API_SECRET))
            }

        def generate_post_body():
            return {
                "customerInternalReference": transaction_id,  # internal reference for the transaction.
                "userReference": user_reference_id,  # internal reference for the user.
                "successUrl": SUCCESS_REDIRECTION_DAPP_URL
            }

        url = f"{JUMIO_BASE_URL}/initiate"
        headers = generate_headers()
        data = generate_post_body()
        request = requests.post(url=url, headers=headers, data=data)

        status = request.status_code
        response = request.json()
        if status != StatusCode.OK:
            raise UnableToInitiateException(response)
        jumio_reference = response["transactionReference"]
        user_verification_repo.add_transaction(transaction_id, user_reference_id, jumio_reference)
        return response

    def submit(self, transaction_id, error_code):
        verification_status = UserVerificationStatus.SUBMIT_SUCCESS.value
        if error_code:
            verification_status = UserVerificationStatus.SUBMIT_ERROR.value
        user_verification_repo.update_verification_status(transaction_id, error_code, verification_status)
        return "OK"

    def complete(self, payload):
        user_verification_repo.complete_transaction(payload)
        return "OK"

    def get_status(self, username):
        user_reference_id = get_user_reference_id_from_username(username)
        status = user_verification_repo.get_status(user_reference_id)
        return status

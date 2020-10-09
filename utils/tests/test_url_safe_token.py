from itsdangerous import BadSignature, SignatureExpired
from pytest import fail 

from notifications_utils.url_safe_token import generate_token, check_token

def test_should_return_payload_from_signed_token():
	payload = 'email@somthing.com'
	token = generate_token(payload, 'secret-key', 'dangerous-salt')
	assert payload == check_token(token, 'secret-key', 'dangerous-salt', 30)






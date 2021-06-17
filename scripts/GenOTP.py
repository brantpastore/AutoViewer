import pyotp
import time

def RetrieveToken():
	base32secret = 'Secret' # Secret Key (We could do things like store this in a vault, this hardcode is temporary)

	totp = pyotp.TOTP(base32secret) # Call pyOTP TOTP with Secret key
	print('Retrieving OTP Code..')
	rtotp = totp.now()
	return rtotp # Return generated code

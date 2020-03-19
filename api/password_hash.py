import hashlib


def make_encrypt(raw_password, salt):
	mod_password = hashlib.sha224(raw_password.encode()).hexdigest()+"__"+salt
	encypt_password = hashlib.sha256(mod_password.encode()).hexdigest()

	return encypt_password
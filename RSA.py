import rsa

def get_keys(bits):
	(pubkey, privkey) = rsa.newkeys(bits)
	return pubkey, privkey

def encrypt(msg, pubkey):
	return rsa.encrypt(msg, pubkey)

def decrypt(msg, privkey):
	return rsa.decrypt(msg, privkey)
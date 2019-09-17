import rsa
import os

def get_keys(bits):
	(pubkey, privkey) = rsa.newkeys(bits)
	return pubkey, privkey

def encrypt(msg, pubkey):
	return rsa.encrypt(msg, pubkey)

def decrypt(msg, privkey):
	return rsa.decrypt(msg, privkey)

def encrypt_blocks(paths, pubkey):
	enc_blocks = []
	for path in paths:
		file = open(path,'r')
		text = file.read()
		ent = text.encode('utf8')
		enc = encrypt(ent, pubkey)
		enc_blocks.append(enc)
		file.close()
		os.system('del '+path)
	return enc_blocks
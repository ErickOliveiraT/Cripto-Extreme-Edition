import serializer
import ArDVK64
import cripto8
import time
import RSA
import eel

eel.init('gui')

@eel.expose
def encrypt(tesseractPass, msg):
	tesseractPass = str(tesseractPass)
	ent = str(msg)
	print(' Loading your keys\n ')
	serializer.recover_keyfile(tesseractPass)
	serializer.unzip_all()
	serializer.recover_all(tesseractPass)
	r1, r2, r3 = serializer.read_cripto8_rotors()
	public, private = serializer.read_rsa_keys()
	serializer.del_keys()
	print(' Keys Loaded\n')
	c8out = cripto8.encode(ent, r1, r2, r3)
	ardvkOut = ArDVK64.encode(c8out)
	if len(ardvkOut) > 500:
		tmp_paths = serializer.divide_in_blocks(ardvkOut)
		enc_blocks = RSA.encrypt_blocks(tmp_paths, public)
		serializer.save_enc_blocks(enc_blocks)
		print("\n Text encrypted. The output is all CriptoOutputX.data files. You can zip them with you want.\n")
		print(" You should hide criptoExtreme_keys.cripto file. This contains all the keys to decrypt CriptoOutput.txt\n")
	else:
		ent = ardvkOut.encode('utf8')
		enc = RSA.encrypt(ent, public)
		serializer.save_output(enc)
		print("\n Text encrypted. The output is in CriptoOutput.data\n")
		print(" You should hide criptoExtreme_keys.cripto file. This contains all the keys to decrypt CriptoOutput.data\n")
	
	return True

eel.start('encrypt.html', size=(1250,800))
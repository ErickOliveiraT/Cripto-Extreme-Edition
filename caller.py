import serializer
import ArDVK64
import cripto8
import string
import time
import RSA
import sys
import eel
import os

eel.init('gui')

@eel.expose
def generateKeys(tesseractKey, r1k, r1s, r2k, r2s, r3k, r3s):
	tesseractKey = str(tesseractKey)
	r1k = int(r1k)
	r1s = str(r1s).lower()
	r2k = int(r2k)
	r2s = str(r2s).lower()
	r3k = int(r3k)
	r3s = str(r3s).lower()
	print(" Saving Cripto 8 Credencials\n")
	r1 = cripto8.rotor(r1k, r1s)
	r2 = cripto8.rotor(r2k, r2s)
	r3 = cripto8.rotor(r3k, r3s)
	serializer.write_cripto8_rotors(r1,r2,r3)
	print(" Cripto 8 Credencials Saved\n")
	print(" Calculating RSA Keys (Be patient, it may take some minutes depending on your computer performance)\n ")
	inicio = time.time()
	public, private = RSA.get_keys(4096)
	fim = time.time()
	print(" RSA Key Calculated - Elapsed time: {} s\n".format(round(fim-inicio,2)))
	print(" Saving RSA Credencials\n")
	serializer.write_rsa_public(public)
	serializer.write_rsa_private(private)
	print(" RSA Credencials Saved\n")
	print(" Encrypting your keys\n ")
	serializer.destroy_all(tesseractKey)
	serializer.zip_all()
	serializer.destroy_keyfile(tesseractKey)
	print(" All keys are now defined. You can now CRIPTO your data!\n")
	print(" You should hide criptoExtreme_keys.cripto This contains all your keys.\n")
	return True

@eel.expose
def encrypt(tesseractKey, msg):
	tesseractKey = str(tesseractKey)
	#keyfile = str(keyfile)
	keyfile = 'criptoExtreme_keys.cripto'
	msg = str(msg)
	print(' Loading your keys\n ')
	serializer.recover_keyfile(tesseractKey)
	serializer.unzip_all()
	serializer.recover_all(tesseractKey)
	r1, r2, r3 = serializer.read_cripto8_rotors()
	public, private = serializer.read_rsa_keys()
	serializer.del_keys()
	print(' Keys Loaded\n')
	ent = msg
	c8out = cripto8.encode(ent, r1, r2, r3)
	ardvkOut = ArDVK64.encode(c8out)
	if len(ardvkOut) > 500:
		tmp_paths = serializer.divide_in_blocks(ardvkOut)
		enc_blocks = RSA.encrypt_blocks(tmp_paths, public)
		serializer.save_enc_blocks(enc_blocks)
		print("\n Text encrypted. The output is all CriptoOutputX.data files. You can zip them with you want.\n")
		print(" You should hide criptoExtreme_keys.zip file. This contains all the keys to decrypt CriptoOutput.txt\n")
	else:
		ent = ardvkOut.encode('utf8')
		enc = RSA.encrypt(ent, public)
		serializer.save_output(enc)
		print("\n Text encrypted. The output is in CriptoOutput.data\n")
		print(" You should hide criptoExtreme_keys.cripto file. This contains all the keys to decrypt CriptoOutput.data\n")
	return True









eel.start('encrypt.html', size=(1250,800))
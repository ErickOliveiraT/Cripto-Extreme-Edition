import serializer
import ArDVK64
import cripto8
import time
import RSA
import eel

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

eel.start('keys.html', size=(1250,800))
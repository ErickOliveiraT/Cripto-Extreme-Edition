import serializer
import ArDVK64
import cripto8
import string
import time
import RSA
import sys
import os

clear = lambda: os.system('cls')
pause = lambda: os.system('pause')

def verifyKey(key):
	if key > 25 or key < 1:
		print('\n Error: Invalid number')
		sys.exit()

def verifyShowing(showing):
	pos = string.ascii_letters
	if pos.find(showing) == -1 or len(showing) > 1:
		print('\n Error: Invalid input')
		sys.exit()

def exists_keyFile():
	try:
		file = open('criptoExtreme_keys.zip','rb')
	except:
		return False
	return True

def exists_EncryptedFile():
	try:
		file = open('CriptoOutput.txt','rb')
	except:
		return False
	return True

def maxLengthAdvise(l):
	if l > 501:
		print("\n Unfortunately, this input is too big for Cripto Extreme Edition v2.0. Try a smaller one.\n")
		print(" Cripto S.A is working to improve this function. Thank you!\n")
		pause()
		clear()
		menu()
	pass

def menu():
	print('\t Welcome to Cripto Extreme Edition v2.0\n')
	print(' 1 - Define Keys\n 2 - Encrypt\n 3 - Decrypt\n 4 - Exit\n')
	op = input(' Option: ')
	if op == '1':
		clear()
		print("\t Define keys\n\n Let's define your Cripto 8 Credencials\n")
		r1K = int(input(' Enter a number between 1 and 25: '))
		verifyKey(r1K)
		r2K = int(input(' Enter a number between 1 and 25: '))
		verifyKey(r2K)
		r3K = int(input(' Enter a number between 1 and 25: '))
		verifyKey(r3K)
		r1s = input(" Enter a letter: ")
		verifyShowing(r1s)
		r2s = input(" Enter a letter: ")
		verifyShowing(r2s)
		r3s = input(" Enter a letter: ")
		verifyShowing(r3s)
		print("\n Cripto 8 Credencials Defined\n")
		r1s = r1s.lower()
		r2s = r2s.lower()
		r3s = r3s.lower()
		print(" Saving Cripto 8 Credencials\n")
		r1 = cripto8.rotor(r1K, r1s)
		r2 = cripto8.rotor(r2K, r2s)
		r3 = cripto8.rotor(r3K, r3s)
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
		serializer.destroy_all('V3E4N86xftJVu2qp')
		time.sleep(1)
		serializer.zip_all()
		print(" All keys are now defined. You can now CRIPTO your data!\n")
		print(" You should hide criptoExtreme_keys.zip. This contains all your keys.\n")
		pause()
		clear()
		menu()
	elif op == '2':
		clear()
		print('\t Encrypt\n')
		if not exists_keyFile():
			print(" You did not defined your keys. Please do this before.\n")
			print(" If you did, make sure you have criptoExtreme_keys.zip file in this folder.\n")
			sys.exit()
		print(' Loading your keys\n ')
		serializer.unzip_all()
		serializer.recover_all('V3E4N86xftJVu2qp')
		time.sleep(1)
		r1, r2, r3 = serializer.read_cripto8_rotors()
		public, private = serializer.read_rsa_keys()
		serializer.destroy_all('V3E4N86xftJVu2qp')
		time.sleep(1)
		serializer.zip_all()
		print(' Keys Loaded\n')
		ent = input(" Enter your message: ")
		c8out = cripto8.encode(ent, r1, r2, r3)
		ardvkOut = ArDVK64.encode(c8out)
		maxLengthAdvise(len(ardvkOut))
		ent = ardvkOut.encode('utf8')
		enc = RSA.encrypt(ent, public)
		serializer.save_output(enc)
		print("\n Text encrypted. The output is in CriptoOutput.txt\n")
		print(" You should hide criptoExtreme_keys.zip file. This contains all the keys to decrypt CriptoOutput.txt\n")
		os.system('CriptoOutput.txt')
		pause()
		clear()
		menu()
	elif op == '3':
		clear()
		print('\t Decrypt\n')
		if not exists_keyFile():
			print(" You did not defined your keys. Please do this before.\n")
			print(" If you did, make sure you have criptoExtreme_keys.zip file in this folder.\n")
			sys.exit()
		print(' Loading your keys\n ')
		serializer.unzip_all()
		serializer.recover_all('V3E4N86xftJVu2qp')
		time.sleep(1)
		r1, r2, r3 = serializer.read_cripto8_rotors()
		public, private = serializer.read_rsa_keys()
		serializer.destroy_all('V3E4N86xftJVu2qp')
		time.sleep(1)
		serializer.zip_all()
		print(' Keys Loaded\n')
		print(' Loading your encripted file\n')
		if not exists_EncryptedFile():
			print(' Error loading your encripted file.\n')
			print(' Make sure you have CriptoOutput.txt file in this folder.\n')
			pause()
			clear()
			menu()
		data = serializer.load_output()
		print(' Encripted file loaded\n')
		print(' Decrypting your text\n')
		dec = RSA.decrypt(data,private)
		plain = ArDVK64.decode(dec.decode())
		out = cripto8.decode(plain, r1, r2, r3)
		print(' Text Decrypted\n\n')
		print(' Your text:\n')
		print(out + '\n\n')
		pause()
		clear()
		menu()
	elif op == '4':
		sys.exit()
	elif op != '1' and op != '2' and op != '3' and op != '4':
		clear()
		menu()

os.system('color 0a')
menu()
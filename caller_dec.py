import serializer
import ArDVK64
import cripto8
import time
import RSA
import eel
import os

eel.init('gui')

@eel.expose
def decrypt(tesseractPass, qntFiles):
	tesseractPass = str(tesseractPass)
	files_qnt = int(qntFiles)
	print(' Loading your keys\n ')
	serializer.recover_keyfile(tesseractPass)
	serializer.unzip_all()
	serializer.recover_all(tesseractPass)
	r1, r2, r3 = serializer.read_cripto8_rotors()
	public, private = serializer.read_rsa_keys()
	serializer.del_keys()
	print(' Keys Loaded\n')
	print('\n Loading your encripted(s) file\n')
	if files_qnt == 1:
		data = serializer.load_output()
		print(' Encripted file loaded\n')
		print(' Decrypting your text\n')
		dec = RSA.decrypt(data,private)
		plain = ArDVK64.decode(dec.decode())
		out = cripto8.decode(plain, r1, r2, r3)
		print(' Text Decrypted\n\n')
		print(' Your text:\n')
		print(out + '\n\n')
		file = open('CriptoDecodedFile.txt','w')
		file.write(out)
		file.close()
		os.system('CriptoDecodedFile.txt')
	elif files_qnt > 1:
		filenames = serializer.get_file_paths(files_qnt)
		outputs = RSA.decrypt_blocks(filenames, private)
		print(' Decrypting your text\n')
		main_ArDVK64_input = ''
		for out in outputs:
			main_ArDVK64_input += out
		dec = ArDVK64.decode(main_ArDVK64_input)
		plain = cripto8.decode(dec, r1, r2, r3)
		print(' Text Decrypted\n\n')
		print(' Your text:\n')
		print(plain + '\n\n')
		file = open('CriptoDecodedFile.txt','w')
		file.write(plain)
		file.close()
		os.system('CriptoDecodedFile.txt')


eel.start('decrypt.html', size=(1250,800))
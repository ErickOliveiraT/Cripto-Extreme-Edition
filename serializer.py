from zipfile import ZipFile
from rsa import key
import cripto8
import time
import os

file_ext = ''

def write_rsa_public(public):
	filename = 'rsa_public' + file_ext 
	file = open(filename,'w')
	n = str(public.n)
	e = str(public.e)
	file.write(n + '\n')
	file.write(e)
	file.close()

def write_rsa_private(private):
	filename = 'rsa_private' + file_ext 
	file = open(filename,'w')
	p = str(private.p)
	q = str(private.q)
	d = str(private.d)
	file.write(p + '\n')
	file.write(q + '\n')
	file.write(d)
	file.close()

def get_public_keys(file):
	keys = []
	for row in file:
		tmp = row.split()
		keys.append(tmp[0])
	n = int(keys[0])
	e = int(keys[1])
	return n, e

def get_private_keys(file):
	keys = []
	for row in file:
		tmp = row.split()
		keys.append(tmp[0])
	p = int(keys[0])
	q = int(keys[1])
	d = int(keys[2])
	return p, q, d

def read_rsa_keys():
	file_public = open('rsa_public','r')
	file_private = open('rsa_private','r')
	n, e = get_public_keys(file_public)
	p, q, d = get_private_keys(file_private)
	file_public.close()
	file_private.close()
	obj_public = key.PublicKey(n, e)
	obj_private = key.PrivateKey(n, e, d, p, q)
	return obj_public, obj_private

def write_cripto8_rotors(r1, r2, r3):
	filename = 'cripto8_rotors' + file_ext 
	file = open(filename,'w')
	r1_info = str(r1.key)+'\n'+r1.showing+'\n'
	r2_info = str(r2.key)+'\n'+r2.showing+'\n'
	r3_info = str(r3.key)+'\n'+r3.showing
	file.write(r1_info)
	file.write(r2_info)
	file.write(r3_info)
	file.close()

def read_cripto8_rotors():
	filename = 'cripto8_rotors' + file_ext 
	file = open(filename,'r')
	rotor_info = []
	for row in file:
		tmp = row.split()
		rotor_info.append(tmp[0])
	file.close()
	r1 = cripto8.rotor(int(rotor_info[0]),rotor_info[1])
	r2 = cripto8.rotor(int(rotor_info[2]),rotor_info[3])
	r3 = cripto8.rotor(int(rotor_info[4]),rotor_info[5])
	return r1, r2, r3

def zip_all():
	file_paths = ['enc_cripto8_rotors'+file_ext,'enc_rsa_public'+file_ext,'enc_rsa_private'+file_ext]
	zp = ZipFile('criptoExtreme_keys.zip','w')
	for file in file_paths:
		zp.write(file)
	for file in file_paths:
		os.system('del ' + file)

def unzip_all():
	file_name = 'criptoExtreme_keys.zip'
	with ZipFile(file_name, 'r') as zip:
		zip.extractall()
	os.system('del ' + file_name)

def destroy_all(password):
	file_paths = ['cripto8_rotors'+file_ext,'rsa_public'+file_ext,'rsa_private'+file_ext]
	time.sleep(1)
	for file in file_paths:
		os.system('tesseract ' + password + ' ' + file + ' enc_' + file)
	time.sleep(1)
	for file in file_paths:
		os.system('del ' + file)

def recover_all(password):
	destroyed = ['enc_cripto8_rotors'+file_ext,'enc_rsa_public'+file_ext,'enc_rsa_private'+file_ext]
	new = ['cripto8_rotors'+file_ext,'rsa_public'+file_ext,'rsa_private'+file_ext]
	for i in range(0,3):
		os.system('tesseract ' + password + ' ' + destroyed[i] + ' ' + new[i])
	time.sleep(1)
	for i in range(0,3):
		os.system('del ' + destroyed[i])

def save_output(output):
	file = open('CriptoOutput.txt','wb')
	file.write(output)
	file.close()

def load_output():
	file = open('CriptoOutput.txt','rb')
	content = file.read()
	file.close()
	return content
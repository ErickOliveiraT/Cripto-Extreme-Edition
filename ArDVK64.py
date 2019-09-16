#-----------ArDVK-64--------------
#---Autor: Érick Oliveira  -------
#---Data:  13/09/2018      -------
#---Copyright: Cripto S.A  -------
#---------------------------------

import binascii

global pos #Conjunto de possibilidades

#---Definição do conjunto de possibilidades----
upper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
lower = 'abcdefghijklmnopqrstuvwxyz'
numbers = '0123456789'
special = '/+'
pos = upper + lower + numbers + special
#----------------------------------------------

def to_bin(num): #Converte um número para binário (força 8 bits)
		temp = str(bin(num))
		binary = ''
		if num >= 47 and num <= 57:
			binary += '0'
		if num == 43:
			binary += '0'
		for bit in temp:
			if bit != 'b':
				binary += bit
		return binary

def to_bin(num): #Converte um número para binário (força 8 bits)
		temp = str(bin(num))
		binary = ''
		if num >= 47 and num <= 57:
			binary += '0'
		if num == 43:
			binary += '0'
		for bit in temp:
			if bit != 'b':
				binary += bit
		return binary

def separate(binary, length): #Separa a entrada binária em blocos de 'length' bits
	separated = ''
	cont = 0
	for bit in binary:
		separated += bit
		cont += 1
		if cont == length:
			separated += ' '
			cont = 0
	return separated

def to_dec(string): #Converte binario para decimal
	soma = 0
	exp = len(string)-1
	for i in range(0,len(string)):
		if string[i] == '1':
			soma += 2 ** exp
		exp -= 1
	return soma

def encode(ent): #Realiza a codificação
	binary = ''
	
	#convertendo para hexadecimal
	ent = ent.encode('utf-8')
	ent = ent.hex()
	for letter in ent:
		aux = ord(letter) #Correspondente decimal ASCII
		binary += to_bin(aux)
	if len(binary) % 6 == 0: #Tamanho da entrada é divisível por 6
		binary = separate(binary, 6)
		dif = 0 #Quantidade de zeros a serem acrescentados
	else: #Tamanho da entrada não é divisível por 6
		aux = len(binary)
		while aux % 6 != 0:
			aux += 1
		dif = aux-len(binary) #Quantidade de zeros a serem acrescentados
		for i in range(0,dif): #acrescenta a quantidade de zeros pra ser divisível por 6
			binary += '0'
		binary = separate(binary, 6)
		#colocando o valor em decimal de cada bloco em um vetor
	temp = ''
	vetor = []
	for bit in binary:
		if bit != ' ':
			temp += bit
		else:
			vetor.append(to_dec(temp))
			temp = ''
		#Saída recebe valor correspondente na tabela padrão para cada valor do vetor
	saida = ''
	for i in vetor:
		saida += pos[i]
	saida += str(dif) #Adiciona número de zeros adicionados
	saida = saida[::-1] #Invertendo saída
	return saida

def reduxTo6(string): #reduz n bits para 6 bits
	hexa = ''
	if len(string) == 6:
		return string
	if len(string) == 8:
		for bit in range(2,len(string)):
			hexa += string[bit]
	elif len(string) == 7:
		for bit in range(1,len(string)):
			hexa += string[bit]
	if len(string) < 6:
		dif = 6-len(string)
		for i in range(0,dif):
			hexa += '0'
		for bit in string:
			hexa += bit
	return hexa

def filter(text): #remove ' e b de uma string convertida
	filtered = ''
	for index in range(1,len(text)-1):
		if text[index] != "'":
			filtered += text[index]
		else:
			continue
	return filtered

def decode(pre_ent): #Realiza a decodificação
	binary = ''
	ent = ''
	dif = int(pre_ent[0]) #Número de zeros acrescentados
	
	for index in range(1,len(pre_ent)): #Remove o primeiro elemento
		ent += pre_ent[index]
	ent = ent[::-1]
	
	for char in ent: 
		index = pos.find(char) #Acha a posicao de cada caractere de ent em pos
		reducted = reduxTo6(to_bin(index)) #converte de volta para binário e reduz para 6 bits
		binary += reducted
	
	original = ''
	for i in range(0,len(binary)-dif): #retirando os zeros acrescentados
		original += binary[i]
		plain_text = ''
	temp = ''
	cont = 0
	for bit in binary: #converte binario para string
		temp += bit
		cont += 1
		if cont == 8:
			aux = to_dec(temp)
			plain_text += chr(aux)
			cont = 0
			temp = ''
			
	plain_text = str(binascii.unhexlify(plain_text))
	plain_text = filter(plain_text)
	return plain_text
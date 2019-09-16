import string

global alf
alf = string.ascii_lowercase

class rotor():
	def __init__(self, key, showing):
		self.key = key
		self.showing = showing
		self.pointed = ''
		self.sequence = self.build_sequence()
		self.spins_count = 0

	def rotate(self, backwards):
		if backwards:
			self.showing = self.sequence[25]
		else:
			self.showing = self.sequence[1]
		self.sequence = self.build_sequence()
		self.spins_count += 1

	def point(self, backwards):
		if backwards:
			new_index = self.sequence.find(self.pointed) - self.key
		else:
			new_index = self.sequence.find(self.pointed) + self.key
		if new_index > 25:
			new_index = new_index % 26
		if new_index < 0:
			new_index = 26 + new_index
		return new_index

	def build_sequence(self):
		sequence = ''
		sequence += self.showing
		tmp_index = alf.find(self.showing)
		for i in range(1,26):
			tmp_index += 1
			if tmp_index > 25:
				tmp_index = 0
			sequence += alf[tmp_index]
		return sequence

	def reset_spins(self):
		self.spins_count = 0

def create_data_block(ent, r1, r2, r3):
	out = ''
	pattern = []
	special = string.punctuation + ' ' + '0123456789'
	for char in ent:
		flag_r1 = False
		flag_r2 = False
		flag_r3 = False
		if special.find(char) != -1:
			out += char
			continue
		r1.pointed = char
		r2.pointed = r2.sequence[r1.point(False)]
		r3.pointed = r3.sequence[r2.point(False)]
		out += r3.sequence[r3.point(False)]
		if len(out) != len(ent):
			r1.rotate(False)
			flag_r1 = True
		if r1.spins_count == 26:
			r2.rotate(False)
			flag_r2 = True
			r1.reset_spins()
			if r2.spins_count == 26:
				r3.rotate(False)
				flag_r3 = True
				r2.reset_spins()
				if r3.spins_count == 26:
					r3.reset_spins()
		tmp = []
		tmp.append(flag_r1)
		tmp.append(flag_r2)
		tmp.append(flag_r3)
		pattern.append(tmp)
	return [r1.showing, r2.showing, r3.showing, pattern]

def encode(ent, r1, r2, r3):
	out = ''
	ent = ent.lower()
	special = string.punctuation + ' ' + '0123456789'
	for char in ent:
		if special.find(char) != -1:
			out += char
			continue
		r1.pointed = char
		r2.pointed = r2.sequence[r1.point(False)]
		r3.pointed = r3.sequence[r2.point(False)]
		out += r3.sequence[r3.point(False)]
		if len(out) != len(ent):
			r1.rotate(False)
		if r1.spins_count == 26:
			r2.rotate(False)
			r1.reset_spins()
			if r2.spins_count == 26:
				r3.rotate(False)
				r2.reset_spins()
				if r3.spins_count == 26:
					r3.reset_spins()
	return out

def filter_ent(ent):
	special = string.punctuation + ' ' + '0123456789'
	ent = ent[::-1]
	store = ''
	new_ent = ''
	for i in range(0,len(ent)):
		if special.find(ent[i]) != -1:
			store += ent[i]
		else:
			for j in range(i,len(ent)):
				new_ent += ent[j]
			break
	return [new_ent[::-1], store]

def decode(ent, r1, r2, r3):
	complete = False
	filter_data = filter_ent(ent)
	ent = filter_data[0]
	if filter_data[1] != '':
		complete = True
		stored = filter_data[1]

	special = string.punctuation + ' ' + '0123456789'
	data_block = create_data_block(ent, r1, r2, r3)
	r1.showing = data_block[0]
	r2.showing = data_block[1]
	r3.showing = data_block[2]
	r1.build_sequence()
	r2.build_sequence()
	r3.build_sequence()
	pattern = data_block[3]
	counter = len(pattern)-1	
	ent = ent[::-1]
	pattern.reverse()
	plain = ''

	for char in ent:
		if special.find(char) != -1:
			plain += char
			continue
		r3.pointed = r3.sequence[r3.sequence.find(char)-r3.key]
		r2.pointed = r2.sequence[r3.sequence.find(r3.pointed)-r2.key]
		r1.pointed = r1.sequence[r2.sequence.find(r2.pointed)-r1.key]
		plain += r1.pointed
		if pattern[counter][0] == 1:
			r1.rotate(True)
		if pattern[counter][1] == 2:
			r2.rotate(True)
		if pattern[counter][2] == 3:
			r3.rotate(True)
		counter -= 1
	if complete:
		return plain[::-1]+stored
	return plain[::-1]
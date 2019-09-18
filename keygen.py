import string
import random

pos = list(string.ascii_letters + string.digits)
random.shuffle(pos)
pos = ''.join(pos)

def get_random_password(length):
	password = ''
	for i in range(0,length):
		rd = random.randint(0,len(pos))
		password += pos[rd]
	return password
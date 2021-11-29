import string as st
import random as rd


## list of used 

def generate_random_password(pw_type):
	#lenght of the 2 password types
	lenght_strong = rd.randint(8, 12)
	lenght_weak = rd.randint(6, 8)

	#contents of the password
	random_letters = []	
	up_letters = list(st.ascii_uppercase)
	for l in up_letters:
		if rd.getrandbits(1) == 0:
			random_letters.append(l.lower())
		else:
			random_letters.append(l.upper())

	digits = list(st.digits)
	symbols = list(st.punctuation)

	mandatory_ele = []
	mandatory_ele.append(random_letters.pop(rd.randint(0,len(random_letters)-1)).lower())
	mandatory_ele.append(random_letters.pop(rd.randint(0,len(random_letters)-1)).upper())
	mandatory_ele.append(digits.pop(rd.randint(0,len(digits)-1)))
	mandatory_ele.append(symbols.pop(rd.randint(0,len(symbols)-1)))

	contents_strong = list(random_letters + digits + symbols)
	contents_weak = list(random_letters + digits) 

	temp_str = mandatory_ele
	for u in range(lenght_strong-4):
		temp_str.append(contents_strong.pop(rd.randint(0,len(contents_strong)-1))) 

	temp_wk = mandatory_ele[0:3]
	for u in range(lenght_weak-3):
		temp_wk.append(contents_weak.pop(rd.randint(0,len(contents_weak)-1)))

	rd.shuffle(temp_str)
	rd.shuffle(temp_wk)

	#to string from list
	password_strong = "".join(temp_str)	
	password_weak = "".join(temp_wk)
	
	if pw_type == 'strong': 
		return password_strong 
	elif pw_type == 'weak':
		return password_weak	

if __name__ == '__main__':
	print(generate_random_password('strong')) 
	print(generate_random_password('weak')) 
	pass 

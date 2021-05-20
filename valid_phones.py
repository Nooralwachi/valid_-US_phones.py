import re
def valid_phones(filename):
	with open(filename, 'r') as f:
			for line in f:
				name, phone = line.strip().split('\t')
				pattern = r'^([0-9]{3}[\.|\s|-]){2}[0-9]{4}$|^\([0-9]{3}\)\s[0-9]{3}[\s|-][0-9]{4}$'
				if re.match(pattern, phone):
					print(phone)

valid_phones('phones.txt')
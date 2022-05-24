# ciphering text
# cipher.py

#ti -> TranslatedIndex
#t -> Translated
#si -> SymbolIndex
#s -> Symbols


def encrypt(m, key):
	s = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890 !?.'
	t = ''
	mode = 'encrypt'		
	
	for symbol in m:
		if symbol in s:
			si = s.find(symbol)

			if mode == 'encrypt':
				ti = si + key
			elif mode == 'decrypt':
				ti = si - key

			if ti >= len(s):
				ti = ti - len(s)
			elif ti < 0:
				ti = ti + len(s)

			t = t + s[ti]
		else:
			t = t + symbol

	return t




def decrypt(m, key):
	s = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890 !?.'
	t = ''
	mode = 'decrypt'		
	
	for symbol in m:
		if symbol in s:
			si = s.find(symbol)

			if mode == 'encrypt':
				ti = si + key
			elif mode == 'decrypt':
				ti = si - key

			if ti >= len(s):
				ti = ti - len(s)
			elif ti < 0:
				ti = ti + len(s)

			t = t + s[ti]
		else:
			t = t + symbol

	return t



if __name__ == '__main__':
	encrypt()
	decrypt()



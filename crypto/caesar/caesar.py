# Caesar cipher brute-force
a = "abcdefghijklmnopqrstuvwxyz"
s = input("Ciphertext: ")
for i in range(26):
	r = ""
	for c in s:
		if c.islower():
			r += a[(a.find(c) + i) % 26]
		elif c.isupper():
			r += a[(a.find(c.lower()) + i) % 26].upper()
		else:
			r += c
	print(i, r)

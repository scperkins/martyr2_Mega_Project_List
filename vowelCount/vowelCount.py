
vowels = "aeiou"
running = True
while running:
	strInput = raw_input("Enter a string: ")
	
	count = 0
	for i in strInput:
		if i in vowels:
			count += 1
	print count
	
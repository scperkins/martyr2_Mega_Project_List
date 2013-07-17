print "Welcome to pig latin!"

running = True

while running:
	strInput = raw_input("Enter a word: ")

	if strInput[0] in "aeiou":
		print strInput + "way"

	else: print strInput[1:] +strInput[0] + "ay"


#palindrome.py
print "Check to see if your string is a palindrome"
running = True
while running:
	strInput = raw_input("Enter a string: ")
	if strInput == strInput[::-1]:
		print "It's a palindrome!"

	else: print "Sorry, not a palindrome." 

import random


#Opening a file "dict.txt" which contains a list of words and copying those words into a list *all_words*
dictionary = open("dict.txt","r")
all_words = dictionary.read().split('\n')
dictionary.close()


#Creating a list of usable words which are atleast 5 letters long
words = []
for w in all_words:
	if len(w) < 5:
		continue
	words.append(w)


#Selecting a word at random from the list of usable words
no_of_words = len(words)
word = words[random.randint(0,no_of_words)]


#Creating a jumbled word with the help of shuffle function
jumbled = list(word)
random.shuffle(jumbled)
jumbled = "".join(jumbled)
print "The Anagram is %s : " % (jumbled)


#Determining the number of hints and tries
hints = 2
tries = 0
if len(word) >= 8:
	tries = 5
else:
	tries = 3


#2 random letters of the word which will be used in hints
i1 = random.randint(0,len(word)-1)
i2 = random.choice(range(0,i1) + range(i1+1,len(word)))


#Loop which iterates until the player guesses the word correctly or is out of tries
while tries > 0:
	print ""
	print "You have %d tries left" % (tries)
	print "Press 1 to Enter your Guess\nPress 2 to use a hint(You have %d hints left)" % (hints)
	choice = int(raw_input("Enter Choice: "))
	if choice == 1:
		guess = raw_input("Enter Your Guess: ")
		if guess == word:
			print "Congratulations! You Won!"
			break
		elif tries > 1:
			print "Sorry Wrong Guess, Try Again"
			tries -= 1
		else:
			tries -= 1
	elif choice == 2 and hints > 0:
		hints -= 1
		hint_word = list(word)
		for i in range(len(word)):
			if not (i == i1 or i == i2):
				hint_word[i] = '.' #Replacing all letters (except hints) of the word with '.'
		if hints == 1:
			hint_word[i2] = '.'
		hint_word = "".join(hint_word)
		print "Hint : %s" % (hint_word)
	else:
		print "Sorry, You're out of hints. Try Again"
else:
	print "Sorry, You Lost the Game"
	print "The correct word was %s" % (word)
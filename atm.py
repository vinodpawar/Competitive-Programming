#ATM program to withdraw cash from ATM
notesOf = [2000,500,100]
amount = input("Enter amount: ")
notes = 0

for i in range(len(notesOf)):
	notes = amount / notesOf[i]
	print notes, "notes of", notesOf[i]
	amount = amount % notesOf[i]
	

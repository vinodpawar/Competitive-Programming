#The program takes an input amount from the user and calculates the number of currency 
#notes (in denominations of 2000, 500, and 100) required to represent that amount.
notesOf = [2000, 500, 100]
amount = int(input("Enter amount: "))  #Converts input to integer
notes = 0

for i in range(len(notesOf)):
    notes = amount // notesOf[i]  #Uses integer division
    print(notes, "notes of", notesOf[i])
    amount = amount % notesOf[i]
	

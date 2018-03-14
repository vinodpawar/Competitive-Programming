#A simple cryptography program that replaces the current letter with the fourth letter next to it.
#Programmed in Python v2.7
alphabates = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
inputName = "abcd"

for i in range(len(inputName)):
	for j in range(len(alphabates)):
		if inputName[i] == alphabates[j]:
			print alphabates[j+4]
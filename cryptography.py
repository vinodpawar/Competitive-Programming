#A simple cryptography program that replaces the First letter with the Fourth letter next to it.
#Program is written in Python v2.7
alphabates = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
inputName = "abdcz"
count = 0

for i in range(len(inputName)):
    for j in range(len(alphabates)):
        if inputName[i] == alphabates[j]:
            if inputName[i] == "w":
                j = -4
            if inputName[i] == "x":
                j = -3
            if inputName[i] == "y":
                j = -2
            if inputName[i] == "z":
                j = -1
            print alphabates[j+4]

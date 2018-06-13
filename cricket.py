#input score provided
inputScore = [1,".",2,"w","W",6,".",2,"b",3,4]

#challenge input:
#inputScore = ["W","W","W","W","W","W","W","W","W","W"]
#inputScore = [1,".",".",2,4,".","w",6]

#player score initialization
playerScore = {1:0, 2:0, 3:0, 4:0, 5:0, 6:0, 7:0, 8:0, 9:0, 10:0,11:0}

#Players, Players on strike, Players on non-strike, Ball count, Score, extras and overs initialization
players = [1,2,3,4,5,6,7,8,9,10,11]
playerOnStrike = players[0]
playerOnNonStrike = players[0+1]
ballCount = 0
score = 0
extras = 0
overs = 0

#loop to operate on given input score
for i in range(len(inputScore)):

	ballCount = ballCount + 1

	if ballCount == 6:
		overs = overs + 1
		temp = playerOnStrike
		playerOnStrike = playerOnNonStrike
		playerOnNonStrike = temp
		ballCount = 0



	#extras-bye
	if inputScore[i] == "b":
		extras = extras + 1
		#tip: do not consider ball here
		ballCount = ballCount - 1

	#wicket
	elif inputScore[i] == "W":
		if playerOnNonStrike > playerOnStrike:
			playerOnStrike = playerOnNonStrike + 1
			if playerOnStrike == 11:
				break

		else:
			playerOnStrike = playerOnStrike + 1
			if playerOnStrike == 11:
				break


	#extras-wide
	elif inputScore[i] == "w":
		extras = extras + 1
		#tip: do not consider ball here
		ballCount = ballCount - 1

	#add score to player
	elif type(inputScore[i]) == int:
		playerScore[playerOnStrike] = playerScore[playerOnStrike] + inputScore[i]
		score = score + inputScore[i]

		#strike change on odd runs
		if inputScore[i] % 2 == 1:
			temp = playerOnStrike
			playerOnStrike = playerOnNonStrike
			playerOnNonStrike = temp

score = score + extras

#print final output scores
lastPlayer = 0
if playerOnStrike > playerOnNonStrike:
	lastPlayer = playerOnStrike + 1

else:
	lastPlayer = playerOnNonStrike + 1

#printing score of all players who have been on the ground
i = 1
while lastPlayer > i:
	print ("P", i , ":", playerScore[i])
	i += 1

print ("Extras:",extras)

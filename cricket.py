inputScore = [1,".",2,"w","W",6,".",2,"b",3,4]

#player_score_initialization
playerScore = {1:0, 2:0, 3:0, 4:0, 5:0, 6:0, 7:0, 8:0, 9:0, 10:0}

#player initialization
players = [1,2,3,4,5,6,7,8,9,10]

#Setting striker and non-striker
playerOnStrike = players[0]
playerOnNonStrike = players[0+1]

#some more initialization
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
		playerOnNonStrike = playerOnStrike
		ballCount = 0

	#extras-bye
	if inputScore[i] == "b":
		extras = extras + 1

	#wicket
	elif inputScore[i] == "W":	

		if playerOnNonStrike > playerOnStrike:
			playerOnStrike = playerOnNonStrike + 1
			#print playerOnStrike, "I am from wicket"
		else:
			playerOnStrike = playerOnStrike + 1
			#print playerOnStrike, "I am from else player onstrike"
	
	#extras-wide
	elif inputScore[i] == "w":
		extras = extras + 1
	
	#dot-ball
	elif inputScore[i] == ".":
		ballCount = ballCount + 1
		#print "Dot ball"

	#add score to player
	elif type(inputScore[i]) == int:
		playerScore[playerOnStrike] = playerScore[playerOnStrike] + inputScore[i]
		score = score + inputScore[i]
		#strike change on odd runs
		if inputScore[i] % 2 == 1:
			temp = playerOnStrike
			playerOnStrike = playerOnNonStrike
			playerOnNonStrike = playerOnStrike
		
score = score + extras
print "Total overs:",overs,"overs and",ballCount, "ball"
print "Total score: ",score

print "Score of Player 1: ", playerScore[1]
print "Score of Player 2: ", playerScore[2]
print "Score of Player 3: ", playerScore[3]
print "Score of Player 4: ", playerScore[4]
print "Score of Player 5: ", playerScore[5]
print "Score of Player 6: ", playerScore[6]
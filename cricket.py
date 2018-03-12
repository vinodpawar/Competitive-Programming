inputScore = [1,".",2,"w","W",6,".",2,"b",3,4]

players = ["P1","P2","P3","P4","P5","P6","P7","P8","P9","P10"]

#player_score_initialization
P1 = 0
P2 = 0
P3 = 0
P4 = 0
P5 = 0
P6 = 0
P7 = 0
P8 = 0
P9 = 0
P10 = 0

playerOnStrike = 1
playerOnNonStrike = 2

ballCount = 0
score = 0
extras = 0
overs = 0



for i in range(len(inputScore)):


	#extras-bye
	if inputScore[i] == "b":
		extras = extras + 1

	#extras-wide
	elif inputScore[i] == "w":
		extras = extras + 1

	#dot-ball
	elif inputScore[i] == ".":
		ballCount = ballCount + 1
		print "Dot ball"

	#wicket
	elif inputScore[i] == "W":
		if playerOnNonStrike > playerOnStrike:
			playerOnStrike = playerOnNonStrike + 1
		else:
			playerOnStrike = playerOnStrike + 1
 
	#score
	#add score to player
	elif type(inputScore[i]) == int:
		score = score + inputScore[i] 
		P1 = P1 + inputScore[i] 
	#strike change on odd runs
	if inputScore[i] % 2 == 1:
		temp = playerOnStrike
		playerOnStrike = playerOnNonStrike
		playerOnNonStrike = playerOnStrike

	#ball-count
	ballCount = ballCount + 1
	print ballCount

	if ballCount == 6:
		overs = overs + 1
		temp = playerOnStrike
		playerOnStrike = playerOnNonStrike
		playerOnNonStrike = temp
		ballCount = 0

score = score + extras
print "Total overs:",overs,"overs and",ballCount, "ball"
print "Total score: ",score
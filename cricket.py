inputScore = [1,".",2,"w","W",6,".",2,"b",3,4]
P1,P2,P3,P4,P5,P6,P7,P8,P9,P10 = 0
playerOnGround = 1
playerOnStrike = 0
strike = P1
ballCount = 0
score = 0
extras = 0
overs = 0
batsmanRemaining = 9


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
#playerOnStrike = playerOnGround + 1
#batsmanRemaining = batsmanRemaining - 1

P1 
 
#score
elif type(inputScore[i]) == int:
score = score + inputScore[i] 

if inputScore[i] % 2 == 1:
playerOnStrike = playerOnGround + 1

P1 = 

#ball-count
ballCount = ballCount + 1
print ballCount

if ballCount == 6:
overs = overs + 1
playerOnStrike = playerOnGround
ballCount = 0

score = score + extras
print "Total overs:",overs,"overs and",ballCount, "ball"
print "Total score: ",score